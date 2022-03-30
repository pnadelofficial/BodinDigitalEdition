$(document).ready(function(){
    $(".fixed-bottom").hide()
})

$(document).on("click","word", function(){
    $(".fixed-bottom").toggle()
    $("p").remove()

    if($(this).parent().parent().prop("tagName") == 'CHAP_FR'){
        $(".col-8").children().remove()
        if(($(this).attr('partofspeech') == 'PROPN') || ($(this).attr('partofspeech') == 'NOUN')){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=2" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if(($(this).attr('partofspeech') == 'AUX') || ($(this).attr('partofspeech') == 'VERB')){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=20" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if(($(this).attr('partofspeech') == 'DET') && ($(this).attr("features").split("|")[0].split("=")[1] == 'Ind')){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=12" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if(($(this).attr('partofspeech') == 'DET') && ($(this).attr("features").split("|")[0].split("=")[1] == 'Def')){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=9" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if(($(this).attr('partofspeech') == 'PRON') && ($(this).attr("features").split("|")[0].split("=")[0] == 'Person')){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=14" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if(($(this).attr('partofspeech') == 'ADV') && ($(this).attr("features").split("|")[0].split("=")[1] == 'Neg')){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=34" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'PRON'){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=39" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'ADJ'){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=16" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'ADV'){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=15" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'ADP'){
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}#page=36" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        }
        else{
            $(".col-8").append(`<object width="100%" height="800px" data="${french_pdf}" type="application/pdf">alt: <a href="${french_pdf}">FRENCH PDF</a></object> `)
        } 
    }
    else if($(this).parent().parent().prop("tagName") == 'CHAP_ENG'){
        $(".col-8").children().remove()
        if(($(this).attr('partofspeech') == 'PROPN') || ($(this).attr('partofspeech') == 'NOUN')){
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}#page=2" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }
        if(($(this).attr('partofspeech') == 'AUX') || ($(this).attr('partofspeech') == 'VERB')){
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}#page=16" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'ADJ'){
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}#page=8" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'ADV'){
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}#page=10" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'PRON'){
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}#page=5" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'ADP'){
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}#page=13" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }
        if($(this).attr('partofspeech') == 'CCONJ'){
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}#page=15" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }
        else{
            $(".col-8").append(`<object width="100%" height="800px" data="${english_pdf}" type="application/pdf">alt: <a href="${english_pdf}">ENGLISH PDF</a></object> `)
        }       
    }
    else{
        $(".col-8").children().remove()
        if($(this).attr("features").split("|")[0].split("=")[1] == 'Nom'){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=16" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        if($(this).attr("features").split("|")[0].split("=")[1] == 'Gen'){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=17" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        if($(this).attr("features").split("|")[0].split("=")[1] == 'Dat'){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=18" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        if($(this).attr("features").split("|")[0].split("=")[1] == 'Acc'){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=20" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        if($(this).attr("features").split("|")[0].split("=")[1] == 'Abl'){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=22" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        if($(this).attr("features").split("|")[0].split("=")[1] == 'Gen'){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=17" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        if((($(this).attr("partofspeech") == 'VERB') || ($(this).attr("partofspeech") == 'AUX')) && ($(this).attr("features").split("|")[0].split("=")[1] != 'Perf')){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=43" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        if($(this).attr("features").split("|")[0].split("=")[1] == 'Perf'){
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}#page=48" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
        else{
            $(".col-8").append(`<object width="100%" height="800px" data="${latin_pdf}" type="application/pdf">alt: <a href="${latin_pdf}">JMH PDF</a></object> `)
        }
    }

    $(".overflow-auto").children().remove()
    $(".overflow-auto").append(`<h2>${$(this).text()}</h2><ul><li>Lemma: ${$(this).attr("lemma")}</li><li>Part of Speech: ${$(this).attr("partofspeech")}</li><li>UD Relation Tag: ${$(this).attr("udrelation")}</li><li>Features: ${$(this).attr("features")}</li></ul>`)
})

$(".fixed-bottom").on("click", "button", function(){
    $(".fixed-bottom").toggle()
})