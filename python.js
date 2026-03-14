async function runPython() {
    let pyodide = await loadPyodide();
    let code = document.getElementById("code").value;

    let result = pyodide.runPython(code);
    document.getElementById("output").textContent = result;
}
