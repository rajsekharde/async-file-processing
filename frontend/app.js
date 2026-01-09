async function uploadFile() {
    const file = document.getElementById("fileInput").files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://lapi-f:8000/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    console.log("UPLOAD:", data);

    watchJob(data.job_id);
}