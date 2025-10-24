async function getFruit() {
    const res = await fetch ("http://127.0.0.1:5000/people");
    const record = await res.json();
    const p = record[0];
    document.getElementById("id").innerHTML = p.id;
    document.getElementById("name").innerHTML = p.name;
    document.getElementById("age").innerHTML = p.age;
    document.getElementById("link").innerHTML = record[0];
}