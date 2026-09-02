// This file connects the HTML page to our Flask backend using fetch()

const form = document.getElementById("job-form");
const jobsBody = document.getElementById("jobs-body");

// Load all jobs when the page opens
document.addEventListener("DOMContentLoaded", loadJobs);

// When the form is submitted, add a new job
form.addEventListener("submit", async (e) => {
  e.preventDefault(); // stop the page from refreshing

  const newJob = {
    company: document.getElementById("company").value,
    role: document.getElementById("role").value,
    date_applied: document.getElementById("date_applied").value,
    status: document.getElementById("status").value,
    notes: document.getElementById("notes").value,
  };

  await fetch("/api/jobs", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newJob),
  });

  form.reset();
  loadJobs(); // refresh the table
});

// Fetch all jobs from the backend and display them
async function loadJobs() {
  const response = await fetch("/api/jobs");
  const jobs = await response.json();

  jobsBody.innerHTML = ""; // clear the table first

  jobs.forEach((job) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${job.company}</td>
      <td>${job.role}</td>
      <td>${job.date_applied || "-"}</td>
      <td>
        <select onchange="updateStatus(${job.id}, this.value)">
          <option value="Applied" ${job.status === "Applied" ? "selected" : ""}>Applied</option>
          <option value="Interview" ${job.status === "Interview" ? "selected" : ""}>Interview</option>
          <option value="Offer" ${job.status === "Offer" ? "selected" : ""}>Offer</option>
          <option value="Rejected" ${job.status === "Rejected" ? "selected" : ""}>Rejected</option>
        </select>
      </td>
      <td>${job.notes || ""}</td>
      <td><button class="delete-btn" onclick="deleteJob(${job.id})">Delete</button></td>
    `;

    jobsBody.appendChild(row);
  });
}

// Update a job's status
async function updateStatus(id, newStatus) {
  await fetch(`/api/jobs/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: newStatus }),
  });
  loadJobs();
}

// Delete a job
async function deleteJob(id) {
  await fetch(`/api/jobs/${id}`, { method: "DELETE" });
  loadJobs();
}
