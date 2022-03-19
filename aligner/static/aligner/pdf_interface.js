   
$(document).on("click","word", function(){
    $("p").remove()

    // $(".col-8").append(`<h2>${$(this).attr("features").split("|")[0]}</h2>`)
    if($(this).parent().parent().prop("tagName") == 'CHAP_FR'){
        $(".col-8").children().remove()
        $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
    }
    else{
        $(".col-8").children().remove()
        $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
    }

    $(".overflow-auto").children().remove()
    $(".overflow-auto").append(`<h2>${$(this).text()}</h2><ul><li>Lemma: ${$(this).attr("lemma")}</li><li>Part of Speech: ${$(this).attr("partofspeech")}</li><li>UD Relation Tag: ${$(this).attr("udrelation")}</li><li>Features: ${$(this).attr("features")}</li></ul>`)
})