/**
 * @param {string} date1
 * @param {string} date2
 * @return {number}
 */
var daysBetweenDates = function(date1, date2) {
  
    dateObj1 = new Date( date1 );
    dateObj2 = new Date( date2 );
        
    return Math.abs(dateObj2-dateObj1) / (1000*60*60*24);

};

console.log( daysBetweenDates( "2020-01-15", "2019-12-31" ) );