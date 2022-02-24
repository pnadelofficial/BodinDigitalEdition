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
          return `<ul><li>Lemma: ${$(this).attr("lemma")}</li><li>Part of Speech: ${$(this).attr("pos")}</li><li>UD Relation Tag: ${$(this).attr("relation")}</li></ul>`
        }
      }
    });
  });
});

// var lookup = []

// $.getJSON('/static/aligner/aligned_indices.json', function(data){
//   $.each(data, function(a,b){
//     //console.log(a)
//     lookup.push(b)
//   })
// })

// $(document).on("click","sentence", function(){
//   if ($(this).parent().prop("tagName") == 'CHAP_FR'){
//     var clickedSentenceID = $(this).attr('sent_id')
    
//   }
// });

// $(document).on("click","word", function(){
//   if($(this).parent().parent().prop("tagName") == 'CHAP_FR'){
//     var clickedWord = $(this).attr('word_id');
//     var clickedAligned = $(this).attr('sent_aligned')
//     $(this).animate({
//       backgroundColor: "yellow"
//     }, 250).delay(500).queue(function(){
//       $(this).animate({
//         backgroundColor: "transparent"
//       }, 500).dequeue();
//     })
//     $("word").each(function(index){
//       if(($(this).attr('align_id') == clickedWord) && ($(this).parent().attr('en_id') == clickedAligned)){
//         $(this).animate({
//           backgroundColor: "yellow"
//         }, 250).delay(500).queue(function(){
//           $(this).animate({
//             backgroundColor: "transparent"
//           }, 500).dequeue();
//         })
//       }
//     });
//   }
//   else{
//     var clickedWord = $(this).attr('align_id');
//     $(this).animate({
//       backgroundColor: "yellow"
//     }, 250).delay(500).queue(function(){
//       $(this).animate({
//         backgroundColor: "transparent"
//       }, 500).dequeue();
//     })
//     $("chap_fr word").each(function(index){
//       if($(this).attr('word_id') == clickedWord){
//         $(this).animate({
//           backgroundColor: "yellow"
//         }, 250).delay(500).queue(function(){
//           $(this).animate({
//             backgroundColor: "transparent"
//           }, 500).dequeue();
//         })
//       }
//     })
//   }
// });