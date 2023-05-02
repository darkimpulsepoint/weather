async function get_videos(search, page){
    let url = "api/videos?search=" + search + "&page="+page
    return await get_json_by_url(url)

}

function search_btn(){
    window.location.href = "?search=" + document.getElementById("searcharea").value
}

async function start(){
    let params = (new URL(document.location)).searchParams;
    let search = params.get("search")
    //
    // if (search==="")
    //     return

    let searcharea = document.getElementById("searcharea")
    searcharea.value=search

    await show_videos()
}

async function show_videos() {
    let searcharea = document.getElementById("searcharea")
    let json = await get_videos(searcharea.value, ((new URL(document.location)).searchParams).get("page"))
    let videos = json.videos
    let results = document.getElementById("results")
    results.innerText = ""

    for (let el in videos) {
        let a = document.createElement("a")

        a.href = "https://pornhub.com" + videos[el]
        a.textContent = el

        results.append(a)
        results.append(document.createElement("br"))
    }

    let ul = document.getElementById("pages")
    let pages = json.pages

    for (let el of pages) {
        let li = document.createElement("li")
        let a = document.createElement("a")
        li.append(a)

        let search_params = (new URL(document.location)).searchParams
        let search = search_params.get("search")
        search = search===null ? "" : search

        a.href = window.location.pathname +"?search=" +search + "&page=" + el
        a.textContent = el

        ul.append(li)
    }
}


async function get_json_by_url(url){
    let response = await fetch(url);
    let json_data
    if (response.ok) {
        json_data = await response.json();
    }
    return json_data
}
