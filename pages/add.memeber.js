import sqlite3 from "sqlite3";
import { open } from "sqlite";
import { v4 as uuidv4 } from "uuid";

async function addTestMember() {
  const db = await open({
    filename: './db.sqlite',
    driver: sqlite3.Database
  });

  const id = uuidv4();
  await db.run(
    "INSERT INTO team_members (id, name, email, role) VALUES (?, ?, ?, ?)",
    [id, "Alice Example", "alice@example.com", "Developer"]
  );

  console.log("Test member added!");
  await db.close();
}

addTestMember().catch(console.error);
