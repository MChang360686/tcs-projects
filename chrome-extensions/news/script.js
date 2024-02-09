async function getFruit() {
    const res=await fetch ("https://api.wheretheiss.at/v1/satellites/25544");
    const record=await res.json();
    console.log(record);
    document.getElementById("date").innerHTML=record.id;
    document.getElementById("articleTitle").innerHTML=setup;
    document.getElementById("author").innerHTML=record.punchline;
    document.getElementById("link").innerHTML=record[0];
}