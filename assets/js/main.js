document.getElementById("invite-form").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const role = document.getElementById("role").value.trim();

  if (!name || !email || !role) {
    alert("Please fill in all fields.");
    return;
  }

  const table = document.getElementById("team-table");
  const row = document.createElement("tr");
  row.innerHTML = `
    <td>
      <div class="d-flex px-2 py-1">
        <div><img src="../assets/img/default-avatar.png" class="avatar avatar-sm me-3" alt="user"></div>
        <div class="d-flex flex-column justify-content-center">
          <h6 class="mb-0 text-sm">${name}</h6>
        </div>
      </div>
    </td>
    <td><p class="text-xs text-secondary mb-0">${email}</p></td>
    <td><p class="text-xs font-weight-bold mb-0">${role}</p></td>
    <td class="align-middle"><a href="#" class="text-secondary font-weight-bold text-xs">Edit</a></td>
  `;
  table.appendChild(row);

  alert(`Invitation sent to ${name} (${email})`);
  document.getElementById("invite-form").reset();

  const modal = bootstrap.Modal.getInstance(document.getElementById("inviteModal"));
  modal.hide();
});
