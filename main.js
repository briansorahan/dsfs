// Data Science from Scratch using either D3 and Go.

// A (possible non-exhaustive) list of references used to make this example:

// | Topic          | URL
// | -------------- | -----------------------------------
// | Axis           | http://bl.ocks.org/mbostock/3019563

main();

function main() {
  var margin    = {top: 20, right: 10, bottom: 20, left: 10},
      padding   = {top: 60, right: 60, bottom: 60, left: 60},
      translate = "translate(" + margin.left + ", " + margin.top + ")",
      outerW    = 960,
      outerH    = 500,
      innerW    = outerW - margin.left - margin.right,
      innerH    = outerH - margin.top  - margin.bottom,
      w         = innerW - padding.left - padding.right,
      h         = innerH - padding.top - padding.bottom,
      x         = d3.scale.linear().domain([0, w]).range([0, w]),
      y         = d3.scale.linear().domain([h, 0]).range([0, h]),
      xAxis     = d3.svg.axis().scale(x).orient("bottom"),
      yAxis     = d3.svg.axis().scale(y).orient("left"),
      svg       = d3.select("body").append("svg");

  var nodes = [ { x: 30,   y: 50   },
                { x: 50,   y: 80   },
                { x: 90,   y: 120  } ];

  var links = [
    { source: nodes[0], target: nodes[1] },
    { source: nodes[2], target: nodes[1] }
  ];

  // Set width and height.
  svg = svg.attr("width", outerW).attr("height", outerH);

  // Apply translation.
  svg = svg.append("g").attr("transform", translate);

  // Axes.
  var g = svg.append("g")
             .attr("transform", "translate(" + padding.left + "," + padding.top + ")");

  g.append("rect")
   .attr("class", "inner")
   .attr("width", w)
   .attr("height", h);

  g.append("g")
   .attr("class", "x axis")
   .attr("transform", "translate(0," + h + ")")
   .call(xAxis);

  g.append("g")
   .attr("class", "y axis")
   .call(yAxis);

  // Draw circles.
  g.selectAll("circle .nodes")
                 .data(nodes)
                 .enter()
                 .append("svg:circle")
                 .attr("class", "nodes")
                 .attr("cx", function(d) { return d.x; })
                 .attr("cy", function(d) { return d.y; })
                 .attr("r", "10px")
                 .attr("fill", "black");

  // Draw lines.
  g.selectAll(".line")
               .data(links)
               .enter()
               .append("line")
               .attr("x1", function(d) { return d.source.x })
               .attr("y1", function(d) { return d.source.y })
               .attr("x2", function(d) { return d.target.x })
               .attr("y2", function(d) { return d.target.y })
               .style("stroke", "rgb(6, 120, 155)");
}
