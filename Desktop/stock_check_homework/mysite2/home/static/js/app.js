// 設定畫圖的width, height,控制其大小
var margin = {top: 20, right: 50, bottom: 30, left: 50},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;
// 設定parse資料時間的格式
var parseDate = d3.timeParse("%Y%m%d");
// 使用techan這個framework拉出以時間為基準的x
var x = techan.scale.financetime()
        .range([0, width]);
var crosshairY = d3.scaleLinear()
        .range([height, 0]);
// K線圖的y
var y = d3.scaleLinear()
        .range([height - 60, 0]);
// 成交量的y
var yVolume = d3.scaleLinear()
        .range([height , height - 60]);


// var sma0 = techan.plot.sma()
//         .xScale(x)
//         .yScale(y);

// var sma1 = techan.plot.sma()
//         .xScale(x)
//         .yScale(y);
// var ema2 = techan.plot.ema()
//         .xScale(x)
//         .yScale(y);
//設定k線圖
var candlestick = techan.plot.candlestick()
        .xScale(x)
        .yScale(y);


var volume = techan.plot.volume()
        .accessor(candlestick.accessor())
        .xScale(x)
        .yScale(yVolume);

var xTopAxis = d3.axisTop(x);
var xAxis = d3.axisBottom()
        .scale(x);
var yRightAxis = d3.axisRight(y);
var yAxis = d3.axisLeft()
        .scale(y);
var volumeAxis = d3.axisRight(yVolume)
        .ticks(3)
        .tickFormat(d3.format(",.3s"));
// 設定十字線左右邊要顯示的文字，根據不同的軸線(yAxis, yRightAxis)來決定
var ohlcAnnotation = techan.plot.axisannotation()
        .axis(yAxis)
        .orient('left')
        .format(d3.format(',.2f'));

var ohlcRightAnnotation = techan.plot.axisannotation()
        .axis(yRightAxis)
        .orient('right')
        .translate([width, 0]);
// 設定十字線上下顯示的時間
var timeAnnotation = techan.plot.axisannotation()
        .axis(xAxis)
        .orient('bottom')
        .format(d3.timeFormat('%Y-%m-%d'))
		.width(80)
        .translate([0, height]);
// 設定十字線
var crosshair = techan.plot.crosshair()
        .xScale(x)
        .yScale(crosshairY)
        .xAnnotation(timeAnnotation)
        .yAnnotation(ohlcAnnotation)
// 設定滑鼠移動過去時要呼叫的function
        .on("move", move);
var textSvg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var svgText = textSvg.append("g")
            .attr("class", "description")
            .append("text")
//            .attr("x", margin.left)
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "start")
            .text("");
//設定畫圖區域
var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var dataArr;
// 讀取data，畫圖
d3.json("api/json_data?stock_code=2603&stock_time={{ time }}", function(error, data) {
    var accessor = candlestick.accessor();
    // var jsonData = data["Data"];
    
    data = 
        data
        .map(function(d) {
        return {
            date: parseDate(d[0]),
            open: +d[1],
            high: +d[2],
            low: +d[3],
            close: +d[4],
            volume: +d[6],
            change: +d[5],
        };
    });
    // 畫candlestick
    svg.append("g")
            .attr("class", "candlestick");
    // svg.append("g")
    //         .attr("class", "sma ma-0");
    // svg.append("g")
    //         .attr("class", "sma ma-1");
    // svg.append("g")
    //         .attr("class", "ema ma-2");
    svg.append("g")
            .attr("class", "volume");
    svg.append("g")
            .attr("class", "volume axis");
    // 畫x, y軸
    svg.append("g")
            .attr("class", "x axis")
            .call(xTopAxis);
    svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
			.call(xAxis);
	svg.append("g")
            .attr("class", "y axis")
            .attr("transform", "translate(" + width + ",0)") //利用translate移動到右邊
            .call(yRightAxis);
    svg.append("g")
            .attr("class", "y axis")
			.call(yAxis);
    svg.append('text')
			.attr("x", 5)
			.attr("y", 15)
			.text("Facebook, Inc. (FB)");
    
    
    // Data to display initially
    draw(data.slice(0, data.length));
    // Only want this button to be active if the data has loaded
    d3.select("button").on("click", function() { draw(data); }).style("display", "inline");
});

function draw(data) {
//   console.log(data); 
    x.domain(data.map(candlestick.accessor().d));
    y.domain(techan.scale.plot.ohlc(data, candlestick.accessor()).domain());
    dataArr = data;
    
    svg.selectAll("g.x.axis").call(xAxis.ticks(7).tickFormat(d3.timeFormat("%m/%d")).tickSize(-height, -height));
    svg.selectAll("g.y.axis").call(yAxis.ticks(10).tickSize(-width, -width));
    yVolume.domain(techan.scale.plot.volume(data).domain());
    var volumeData = data.map(function(d){return d.volume;});
    svg.append("g")
        .attr("class", "crosshair")
        .call(crosshair)
    
    svg.select("g.volume").datum(data)
        .call(volume);
    
    var state = svg.selectAll("g.candlestick").datum(data);
    state.call(candlestick);
    
    
    // svg.select("g.sma.ma-0").datum(techan.indicator.sma().period(10)(data)).call(sma0);
    // svg.select("g.sma.ma-1").datum(techan.indicator.sma().period(20)(data)).call(sma0);
    // svg.select("g.ema.ma-2").datum(techan.indicator.sma().period(50)(data)).call(sma0);

    svg.select("g.volume.axis").call(volumeAxis);

}


function move(coords) {
    var i;
    for (i = 0; i < dataArr.length; i ++) {
        if (coords.x === dataArr[i].date) {
            svgText.text(d3.timeFormat("%Y/%m/%d")(coords.x) + ", 開盤：" + dataArr[i].open + ", 高：" + dataArr[i].high + ", 低："+ dataArr[i].low + ", 收盤："+ dataArr[i].close + ", 漲跌：" + dataArr[i].change + ", 成交量： " + dataArr[i].transaction);
        }
    }
}










