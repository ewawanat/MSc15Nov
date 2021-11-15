const dims = {height: 300, width: 300, radius: 150};
const cent = {x: (dims.width/2 + 5), y: (dims. height/2 + 5)};

const svg = d3.select('.canvas')
    .append('svg')
    .attr('width', dims.width + 150)
    .attr('height', dims.height + 150)

const graph = svg.append('g')
    .attr('transformm', `translate(${cent.x}), ${cent.y})`);

    //function which generates angles: 
const pie = d3.pie()   
    .sort(null)
    .value(d => d.frequency);


//const angles = pie(data.json);

const arcPath = d3.arc()
    .outerRadius(dims.radius)
    .innerRadius(dims.radius/2);

const colour = d3.scaleOrdinal(d3['schemeSet3'])

const paths = graph.selectAll('path')
    .data(pie(data));

const arcTweenEnter = (d) => {
    var i = d3.interpolate(d.endAngle-0.1, d.startAngle);
        
    return function(t){
        d.startAngle = i(t);
        return arcPath(d);            
    }    
}

paths.enter()
  .append('path')
    .attr('class', 'arc')
    .attr('stroke', '#fff')
    .attr('stroke-width', 3)
    .attr('fill', d => colour(d.data.species_name))
    .transition().duration(1500)
      .attrTween("d", arcTweenEnter);