function ermify(){
    let txt = document.getElementById("ermify");
    if(txt.value == ""){
        console.log("no text inputted :(");
    }else{
        fetch("/ermify", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"data":txt.value})
        })

        .then(response => {
            if(!response.ok){
                console.log("response not okay");
            }else{
                return response.json();
            }
        })

        .then(data => {
            if(data.message == "euge"){
                console.log(data.ermified);
                document.getElementById("ermifiedTxt").innerText = data.ermified;
                txt.value = "";
            }else{
                console.log("eheu!");
            }
        })

        .catch(error => {
            console.log(error);
        })
    }
}