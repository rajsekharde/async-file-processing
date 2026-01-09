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

async function showDownloads(jobId, files) {
    const container = document.createElement("div");
    container.className = "testDiv"
    container.innerHTML = "<h3>Results</h3>";

    for (const file of files) {
        const button = document.createElement("button");
        button.textContent = "Download";

        button.addEventListener("click", () => {
            const link = document.createElement("a");
            link.href = `http://api-f:8000/download/${jobId}/${encodeURIComponent(file)}`;
            link.download = file;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
        button.style.display = "block";

        container.appendChild(button);
    }

    document.body.appendChild(container);
}