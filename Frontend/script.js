async function generateText() {
     document.getElementById("output").innerText =
    "Generating...";

    const prompt =
        document.getElementById("prompt").value;
    document.getElementById("generateBtn").disabled = true;

    const response =
        await fetch(
            "http://127.0.0.1:5000/generate",
            {
                method: "POST",
                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({
                    prompt: prompt
                })
            }
        );

    const data = await response.json();

    document.getElementById("generateBtn").disabled = false;

    document.getElementById("output")
        .innerText =
        data.generated_text;
}