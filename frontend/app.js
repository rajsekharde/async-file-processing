async function uploadFile() {
    const file = document.getElementById("fileInput").files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://api-f:8000/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    console.log("UPLOAD:", data);

    watchJob(data.job_id);
}

async function fetchFileStatus(jobId) {
    while (true) {
        await new Promise(r => setTimeout(r, 2000));

        const res = await fetch(`http://api-f:8000/status/${jobId}`);
        const data = await res.json();

        if (data.status === "COMPLETED") {
            showDownloads(jobId, data.files);
        }
    }
}