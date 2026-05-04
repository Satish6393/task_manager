const API = "http://127.0.0.1:5000/api";

function signup() {
  fetch(`${API}/auth/signup`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      password: document.getElementById("password").value,
      role: document.getElementById("role").value
    })
  }).then(res => res.json()).then(data => alert(data.message));
}

function login() {
  fetch(`${API}/auth/login`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      email: document.getElementById("loginEmail").value,
      password: document.getElementById("loginPassword").value
    })
  }).then(res => res.json()).then(data => {
    localStorage.setItem("token", data.token);
    window.location.href = "dashboard.html";
  });
}

function loadDashboard() {
  fetch(`${API}/dashboard`, {
    headers: {
      "Authorization": localStorage.getItem("token")
    }
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("data").innerHTML = JSON.stringify(data);
  });
}

function createProject() {
  fetch(`${API}/projects`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": localStorage.getItem("token")
    },
    body: JSON.stringify({
      name: document.getElementById("projectName").value
    })
  }).then(res => res.json()).then(data => alert(data.message));
}

function createTask() {
  fetch(`${API}/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": localStorage.getItem("token")
    },
    body: JSON.stringify({
      title: document.getElementById("title").value,
      description: document.getElementById("desc").value,
      project_id: document.getElementById("projectId").value,
      assigned_to: document.getElementById("assignedTo").value,
      deadline: document.getElementById("deadline").value
    })
  }).then(res => res.json()).then(data => alert(data.message));
}