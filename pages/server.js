// server.js
import express from "express";
import cors from "cors";
import nodemailer from "nodemailer";
import dotenv from "dotenv";
import { v4 as uuidv4 } from "uuid";
import sqlite3 from "sqlite3";
import { open } from "sqlite";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static("pages")); // serve static front-end files

async function startServer() {
  // Initialize SQLite database
  const db = await open({
    filename: "./db.sqlite",
    driver: sqlite3.Database,
  });

  // Create projects table if it doesn't exist
  await db.run(`
    CREATE TABLE IF NOT EXISTS projects (
      id TEXT PRIMARY KEY,
      title TEXT NOT NULL,
      description TEXT,
      start_date TEXT,
      end_date TEXT,
      status TEXT
    )
  `);

  // Create team_members table if it doesn't exist
  await db.run(`
    CREATE TABLE IF NOT EXISTS team_members (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      role TEXT NOT NULL
    )
  `);

  // =======================
  //   PROJECT ROUTES
  // =======================

  // Fetch all projects
  app.get("/projects", async (req, res) => {
    try {
      const rows = await db.all("SELECT * FROM projects ORDER BY start_date ASC");
      const projects = rows.map(r => ({
        id: r.id,
        title: r.title,
        description: r.description,
        startDate: r.start_date,
        endDate: r.end_date,
        status: r.status,
      }));
      res.json(projects);
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: "Failed to fetch projects." });
    }
  });

  // Create new project
  app.post("/projects", async (req, res) => {
    const { title, description, startDate, endDate, status } = req.body;
    if (!title || !description || !startDate || !endDate) {
      return res.status(400).json({ error: "Missing required fields." });
    }

    try {
      const id = uuidv4();
      await db.run(
        `INSERT INTO projects (id, title, description, start_date, end_date, status)
         VALUES (?, ?, ?, ?, ?, ?)`,
        [id, title, description, startDate, endDate, status]
      );
      res.json({ message: "Project added successfully", id });
    } catch (err) {
      console.error("Error adding project:", err);
      res.status(500).json({ error: "Failed to add project." });
    }
  });

  // Update existing project
  app.put("/projects/:id", async (req, res) => {
    const { id } = req.params;
    const { title, description, startDate, endDate, status } = req.body;
    try {
      await db.run(
        `UPDATE projects SET title=?, description=?, start_date=?, end_date=?, status=? WHERE id=?`,
        [title, description, startDate, endDate, status, id]
      );
      res.json({ message: "Project updated." });
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: "Failed to update project." });
    }
  });

  // Delete project
  app.delete("/projects/:id", async (req, res) => {
    const { id } = req.params;
    try {
      await db.run("DELETE FROM projects WHERE id=?", [id]);
      res.json({ message: "Project deleted." });
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: "Failed to delete project." });
    }
  });

  // =======================
  //   TEAM MEMBER ROUTES
  // =======================

  app.get("/team-members", async (req, res) => {
    try {
      const members = await db.all("SELECT * FROM team_members ORDER BY name ASC");
      res.json(members);
    } catch (err) {
      console.error("Error fetching team members:", err);
      res.status(500).json({ error: "Failed to fetch team members." });
    }
  });

  const PORT = process.env.PORT || 5000;
  app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
}

// Launch server
startServer().catch((err) => {
  console.error("Failed to start server:", err);
});
