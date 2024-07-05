document.addEventListener('DOMContentLoaded', function () {
    var graphs = document.querySelectorAll('#graph');
    graphs.forEach(function (graph) {
        Plotly.react(graph.id, graph.data, graph.layout);
    });
});
