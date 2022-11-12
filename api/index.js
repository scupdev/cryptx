const app = require('express')();
const PORT = 8000;

app.listen(
    PORT,
    () => console.log(`it is alive on https://localhost:${PORT}`)
)