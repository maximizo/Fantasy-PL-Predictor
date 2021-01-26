  
// import constants that define the route names
import { data_url } from './route_constants.js';

// find the div element where we want to put the list
var div_element = d3.select("#table1");
var ul_element = div_element.append("ul");

// use d3 to get data from flask app
// data_url = "http://127.0.0.1:5000/data1";
d3.json(data_url).then(function(data) {
    for (let [key, value] of Object.entries(data)) {
        ul_element.append("li").text(`${key}: ${value}`)
    }
});