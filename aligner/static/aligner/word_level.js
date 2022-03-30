$(document).ready(function(){
  $("word").attr('data-toggle','tooltip')
  $(function(){
    $('[data-toggle="tooltip"]').tooltip({
          placement: 'auto',
          html: true,
          title: function(){if($(this).attr("feats") != 'undefined'){
          return `<ul><li>Lemma: ${$(this).attr("lemma")}</li><li>Part of Speech: ${$(this).attr("partofspeech")}</li><li>UD Relation Tag: ${$(this).attr("udrelation")}</li><li>Features: ${$(this).attr("features")}</li></ul>`
        }
        else{
          return `<ul><li>Lemma: ${$(this).attr("lemma")}</li><li>Part of Speech: ${$(this).attr("partofspeech")}</li><li>UD Relation Tag: ${$(this).attr("udrelation")}</li></ul>`
        }
      }
    });
  });
});

$(document).on("click","word", function(){
  if($(this).parent().parent().prop("tagName") == 'CHAP_FR'){
    var clickedWord = $(this).attr('word_id');
    var enClickedAligned = $(this).attr('en_sent_aligned')
    var laClickedAligned = $(this).attr('la_sent_aligned')
    $(this).animate({
      backgroundColor: "yellow"
    }, 250).delay(500).queue(function(){
      $(this).animate({
        backgroundColor: "transparent"
      }, 500).dequeue();
    })
    $("word").each(function(){
      if(($(this).attr('align_id') == clickedWord) && (($(this).attr('sent_aligned') == enClickedAligned) || ($(this).attr('sent_aligned') == laClickedAligned))){
        $(this).animate({
          backgroundColor: "yellow"
        }, 250).delay(500).queue(function(){
          $(this).animate({
            backgroundColor: "transparent"
          }, 500).dequeue();
        })
      }
    });
  }
  else if(($(this).parent().parent().prop("tagName") == 'CHAP_ENG')){
    var clickedWord = $(this).attr('align_id')
    var clickedAligned = $(this).attr('sent_aligned')
    $(this).animate({
      backgroundColor: "yellow"
    }, 250).delay(500).queue(function(){
      $(this).animate({
        backgroundColor: "transparent"
      }, 500).dequeue();
    })
    $("word").each(function(){
      if($(this).parent().parent().prop("tagName") == 'CHAP_FR'){
        if(($(this).attr('en_sent_aligned') == clickedAligned) && ($(this).attr('word_id') == clickedWord)){
          $(this).animate({
            backgroundColor: "yellow"
          }, 250).delay(500).queue(function(){
            $(this).animate({
              backgroundColor: "transparent"
            }, 500).dequeue();
          })
        }
      }
    })
  }
  else{
    var clickedWord = $(this).attr('align_id')
    var clickedAligned = $(this).attr('sent_aligned')
    $(this).animate({
      backgroundColor: "yellow"
    }, 250).delay(500).queue(function(){
      $(this).animate({
        backgroundColor: "transparent"
      }, 500).dequeue();
    })
    $("word").each(function(){
      if($(this).parent().parent().prop("tagName") == 'CHAP_FR'){
        if(($(this).attr('la_sent_aligned') == clickedAligned) && ($(this).attr('word_id') == clickedWord)){
          $(this).animate({
            backgroundColor: "yellow"
          }, 250).delay(500).queue(function(){
            $(this).animate({
              backgroundColor: "transparent"
            }, 500).dequeue();
          })
        }
      }
    })
  }
});