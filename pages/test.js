// No imports needed, fetch is built-in in Node 18+

async function testTeamMembers() {
  try {
    const res = await fetch("http://localhost:5000/team-members");
    if (!res.ok) throw new Error("Network response was not ok");
    const data = await res.json();
    console.log("Team members:", data);
  } catch (err) {
    console.error("Failed to fetch team members:", err);
  }
}

testTeamMembers();
