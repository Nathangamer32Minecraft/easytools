const form = document.getElementById("form");
const output = document.getElementById("output");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const fileInput = document.getElementById("file");
  const file = fileInput.files[0];

  if (!file || !file.name.endsWith(".class")) {
    alert("Veuillez sélectionner un fichier .class valide.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    if (!res.ok) {
      const errorText = await res.text();
      output.textContent = "Erreur : " + errorText;
      return;
    }

    const javaCode = await res.text();
    output.textContent = javaCode;
  } catch (err) {
    output.textContent = "Une erreur est survenue : " + err.message;
  }
});
