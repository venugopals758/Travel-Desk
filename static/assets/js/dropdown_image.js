$(document).ready(function() {
    $("#to_user").select2({
      ajax: {
        //url: "https://api.github.com/search/repositories",
        url:'/file/get_to_users',
        type: "POST",
        dataType: 'json',
        delay: 150,
        data: function (params) {
          return {
            term: params.term, // search term

          };
        },
        processResults: function (data) {
            console.log(data)
          return {
            results: data,

          };
        },
        cache: true
      },
      placeholder: 'Search with name/email/designation',
      minimumInputLength: 3,
      templateResult: formatRepo,
      templateSelection: formatRepoSelection
    });

    function formatRepo (repo) {
      if (repo.loading) {
        return repo.text;
      }

      var $container = $(
        "<div class='select2-result-repository clearfix'>" +
          "<div class='select2-result-repository__avatar avatar avatar-sm rounded-circle'><img style='height:50px;width:50px' src='" + repo.image + "' /></div>" +
          "<div class='select2-result-repository__meta'>" +
            "<div class='select2-result-repository__title'></div>" +
            "<div class='select2-result-repository__description'></div>" +

          "</div>" +
        "</div>"
      );

      $container.find(".select2-result-repository__title").text(repo.first_name);
      $container.find(".select2-result-repository__description").text(repo.email+' | '+ repo.designation+' | '+repo.department+' | '+repo.institution+' | '+repo.campus);


      return $container;
    }

    function formatRepoSelection (repo) {
      return repo.full_data || repo.text;
    }

    $("#cc_users").select2({
      ajax: {
        //url: "https://api.github.com/search/repositories",
        url:'/file/get_to_users',
        type: "POST",
        dataType: 'json',
        delay: 150,
        data: function (params) {
          return {
            term: params.term, // search term

          };
        },
        processResults: function (data) {
            console.log(data)
          return {
            results: data,

          };
        },
        cache: true
      },
      placeholder: 'Search with name/email/designation',
      minimumInputLength: 3,
      templateResult: formatRepo,
      templateSelection: formatRepoSelection
    });


    $("#to_user_edit").select2({

      ajax: {
        //url: "https://api.github.com/search/repositories",
        url:'/file/get_to_users',
        type: "POST",
        dataType: 'json',
        delay: 150,
        data: function (params) {
          return {
            term: params.term, // search term

          };
        },
        processResults: function (data) {
            console.log(data)
          return {
            results: data,

          };
        },
        cache: true
      },
      placeholder: 'Search with name/email/designation',
      minimumInputLength: 3,
      templateResult: formatRepo,
      templateSelection: formatRepoSelection
    });

    function formatRepo (repo) {
      if (repo.loading) {
        return repo.text;
      }

      var $container = $(
        "<div class='select2-result-repository clearfix'>" +
          "<div class='select2-result-repository__avatar avatar avatar-sm rounded-circle'><img style='height:50px;width:50px' src='" + repo.image + "' /></div>" +
          "<div class='select2-result-repository__meta'>" +
            "<div class='select2-result-repository__title'></div>" +
            "<div class='select2-result-repository__description'></div>" +

          "</div>" +
        "</div>"
      );

      $container.find(".select2-result-repository__title").text(repo.first_name);
      $container.find(".select2-result-repository__description").text(repo.email+' | '+ repo.designation+' | '+repo.department+' | '+repo.institution+' | '+repo.campus);


      return $container;
    }

    function formatRepoSelection (repo) {
      return repo.full_data || repo.text;
    }

    $("#cc_users").select2({
      ajax: {
        //url: "https://api.github.com/search/repositories",
        url:'/file/get_to_users',
        type: "POST",
        dataType: 'json',
        delay: 150,
        data: function (params) {
          return {
            term: params.term, // search term

          };
        },
        processResults: function (data) {
            console.log(data)
          return {
            results: data,

          };
        },
        cache: true
      },
      placeholder: 'Search with name/email/designation',
      minimumInputLength: 3,
      templateResult: formatRepo,
      templateSelection: formatRepoSelection
    });
})


