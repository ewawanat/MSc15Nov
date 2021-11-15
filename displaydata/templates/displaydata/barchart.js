const svg = d3.select('.canvas')
    .append('svg')
    .attr('width', 600)
    .attr('height', 600);
//create margins and dimensions 

const margin = {top: 20, right: 20, bottom: 100, left: 100}
const graphWidth = 600 - margin.left - margin.right;
const graphHeight = 600 - margin.top - margin. bottom;

const graph = svg.append('g')
    .attr('width', graphWidth)
    .attr('height', graphHeight)
    .attr('transform', `translate(${margin.left}, ${margin.top})`)

const xAxisGroup = graph.append('g')
    .attr('transform', `translate(0, ${graphHeight})`);
const yAxisGroup = graph.append('g');


d3.json('data.json').then(data => {
    //join data to rects

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d=> d.frequency)])
        .range([graphHeight, 0]);


    const x = d3.scaleBand()
        .domain(data.map(item => item.species_name))
        .range([0, 500])
        .paddingInner(0.2)
        .paddingOuter(0.2);

    const rects = graph.selectAll('rect')
        .data(data)

    rects.attr('width', x.bandwidth)
        .attr('height', d => graphHeight - y(d.frequency))
        .attr('fill', 'orange')
        .attr('x', d => x(d.species_name))
        .attr('y', d=> y(d.frequency));

    
    rects.enter()
        .append('rect')
            .attr('width', x.bandwidth)
            .attr('height', 0)
            .attr('fill', 'orange')
            .attr('x', d=> x(d.species_name))
            .attr('y', graphHeight)
            .transition().duration(500)
                .attr('y', d=> y(d.frequency))
                .attr('height', d => graphHeight - y(d.frequency));


    //create and call the axes
    const xAxis = d3.axisBottom(x)
        
    const yAxis = d3.axisLeft(y)
        .tickFormat(d=> d + ' birds');

    xAxisGroup.call(xAxis);
    yAxisGroup.call(yAxis);

    xAxisGroup.selectAll('text')
        .attr('transform', 'rotate(-40)')
        .attr('text-anchor', 'end')
        .attr('fill', 'orange');

});