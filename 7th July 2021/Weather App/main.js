// API Configuration
// ISO2 -> CODE OF COUNTRY


const config = {
    // country url and key
    cUrl: "https://api.countrystatecity.in/v1/countries",
    cKey: "R3NUdUE3RTdlbWt5ckF3WEJLMkFwQ0VJWDNUaThLUGdrU09VZEhuaA==",

    // weather url and key
    wUrl: "https://api.openweathermap.org/data/2.5/",
    wKey: "1e319beb7e35ac5192af864e2221eefe",
};

// function get country
// here fieldname menas country or state or city
// for states we have to fetch -> https://api.countrystatecity.in/v1/countries/[ciso]/states this url 
// but apan using getCountries() function we fetch till countries -> https://api.countrystatecity.in/v1/countries
// now we have to fetch for states so -> /[ciso]/states


// and for cities we have to fetch -> https://api.countrystatecity.in/v1/countries/[ciso]/states/[siso]/cities this url 
// after fetching states we have to fetch for cities -> /[siso]/cities 

// here fieldname menas country or state or city
// ...args is REST operator we can pass many arguments wrap into array
const getCountries = async (fieldName,...args) =>
{
    let apiEndPoint = `${config.cUrl}`;
    //console.log(apiEndPoint);  output -> https://api.countrystatecity.in/v1/countries
    switch(fieldName)
    {
        // if fieldName is country then use endpoint as country
        case "countries":
            apiEndPoint = `${config.cUrl}`;
            break;

        // if fieldName is state then use endpoint as states
        // https://api.countrystatecity.in/v1/countries/[ciso]/states

        case "states":
            // args[0] -> country code
            apiEndPoint = `${config.cUrl}/${args[0]}/states`;
            break;

        // if fieldName is cities then use endpoint as cities 
        // https://api.countrystatecity.in/v1/countries/[ciso]/states/[siso]/cities

        case "cities":
            // ${args[0]} -> state code
            apiEndPoint = `${config.cUrl}/${args[0]}/states/${args[1]}/cities`;
            break;

        default:
    }



    // fetch returns promise so we use await
    // and if we use await then we have to call our function async
    const response = await fetch(apiEndPoint, {headers: {"X-CSCAPI-KEY": config.cKey} } );
    
    // if status is not OK i.e. 200 then throw error and status code 
    if(response.status != 200)
    {
        throw new Error(`Something Went Wrong, Status Code: ${response.status}`)
    }

    // if all okay then we want response in JSON format and json format returns promise so requires await
    const countries = await response.json();
    return countries;
}




// calling getWeather function 
// we are using unit- metric for display temp in celsius 
// for fahrenheit use units=imperial
const getWeather = async (cityName, countryCode, units = "metric") => {
    const apiEndPoint = `${config.wUrl}weather?q=${cityName},${countryCode.toLowerCase()}&APPID=${config.wKey}&units=${units}`;

    // console.log(apiEndPoint); -> https://api.openweathermap.org/data/2.5/weather?q=Ahmadpur,in&APPID=1e319beb7e35ac5192af864e2221eefe&units=metric
    try {
        const response = await fetch(apiEndPoint);

        // console.log(response); -> status: 200

        if (response.status != 200) {
            // 404 error indicates that the webpage you're trying to reach can't be found.
          if (response.status == 404) {
            weatherDiv.innerHTML = `<div class="alert-danger">
                                  <h3>Oops! No data available.</h3>
                                  </div>`;
          } else {
            throw new Error(
              `Something went wrong, status code: ${response.status}`
            );
          }
        }
        // if all okay then 
        const weather = await response.json();
        return weather;
      } catch (error) {
        console.log(error);
      }
    };


    // getDateTime Function 
    const getDateTime = (unixTimeStamp) => {
        const milliseconds = unixTimeStamp * 1000;
        const dateObj = new Date(milliseconds);
        const options = {
            weekday:"long",
            year:"numeric",
            month:"long",
            day:"numeric",
        };
        const humanDateFormat = dateObj.toLocaleDateString('en-US',options);
        return humanDateFormat;
    }

    const displayWeather = (data) =>
    {
        const wheatherWidget = `<div class="card">
        <div class="card-body">
            <h5 class="card-title">${data.name} ${data.sys.country} <span class="float-end units"><a href="#" class="unitlink active" data-unit="cel">°C</a> | <a href="#" data-unit="far" class="unitlink">°F</a> </span> </h5>
            <p>${getDateTime(data.dt)}</p>

            <div id="tempcard">
                <h6 class="card-subtitle mb-2 cel">${data.main.temp}</h6>
                <p class="card-text">Feels Like: ${data.main.temp} °C</p>
                <p class="card-text">Max: ${data.main.temp_max} °C, Min: ${data.main.temp_min} °C</p>
            </div>

            ${data.weather.map(w => `<div id="img-container">${w.main} <img src="https://openweathermap.org/img/wn/${w.icon}.png" alt=""> </div>
            <p>${w.description}</p>`).join('\n')}
            
        </div>
    </div>`

    // here we using map function becaz weather is array of object 
    // we can fetch array of object using index ex. weather[0] index 
    // or using map
    // when we use map then we have to join becaz map will return array 

        weatherDiv.innerHTML = wheatherWidget;
    };




// fetching values of DOM 
const countriesListDropDown = document.querySelector("#countrylist");
const statesListDropDown = document.querySelector("#statelist");
const citiesListDropDown = document.querySelector("#citylist");
const weatherDiv = document.querySelector("#weatherwidget");



// when our DOM content is completely loads then call arrow function

// here we list countries
document.addEventListener('DOMContentLoaded', async () => 
{
    const countries = await getCountries("countries");
    // console.log(countries);

    // check for country 
    
    let countriesOptions = "";
    if(countries)
    {
        countriesOptions += `<option value="">Select Country</option>`;
   
        // countries is array so fetch each country elements from array we use forEach loop
        countries.forEach((country) => {
            countriesOptions += `<option value="${country.iso2}">${country.name}</option>`;
        });

        countriesListDropDown.innerHTML = countriesOptions;
    }


    // check for state now according to country
    // when we click on countriesListDropDown button then we use addEventListener in that we use change and pass one function for state 
    // here we get country code according to country code we will find states

    // here we are using normal function becaz we have to use this keyword to fetch value of selected button 
    // and arrow function does not allow to use this keyword 

    countriesListDropDown.addEventListener("change", async function() 
    {
        const selectedCountryCode = this.value;
        // console.log(selectedCountryCode);  output -> IN

        // here we are using getCountries function to select state
        // here we are passing two arguments i.e. fieldName-> states and ...args-> selectedCountryCode
        // switch case goes for states and args having value country code

        const states = await getCountries("states", selectedCountryCode);
        // console.log(states); // gives array of states of selected country

        let statesOptions = "";
        if(states)
        {
            statesOptions += `<option value="">Select State</option>`;
   
            // countries is array so fetch each country elements from array we use forEach loop
            states.forEach((state) => {
                statesOptions += `<option value="${state.iso2}">${state.name}</option>`;
            });

            statesListDropDown.innerHTML = statesOptions;
            // here in our 
                // <div class="mb-3">
                //     <select name="statelist" id="statelist" class="form-select" disabled>
                //          <option value="">Select State</option>
                //     </select>
                // </div>

            // but in HTML we disabled te aplyala allow kela pahije jevha country select krto tevha lagech state select karay la allow jhala pahije
            statesListDropDown.disabled = false;
        }
    });

    // list cities according to states

    statesListDropDown.addEventListener("change", async function() 
    {
        // we requires both country and state value 
        const selectedCountryCode = countriesListDropDown.value;
        const selectedStateCode = this.value;

        // here we are using getCountries function to select city
        // here we are passing two arguments i.e. fieldName-> cities and ...args-> selectedStateCode
        // switch case goes for states and args having value country code and state code

        const cities = await getCountries("cities", selectedCountryCode, selectedStateCode);
        // console.log(cities); -> gives array of all cities of selected country and selected state 

        let citiesOptions = "";
        if(cities)
        {
            citiesOptions += `<option value="">Select State</option>`;
   
            // countries is array so fetch each country elements from array we use forEach loop
            cities.forEach((city) => {
                citiesOptions += `<option value="${city.name}">${city.name}</option>`;
            });

            citiesListDropDown.innerHTML = citiesOptions;
            // here in our 
                // <div class="mb-3">
                //     <select name="statelist" id="statelist" class="form-select" disabled>
                //          <option value="">Select State</option>
                //     </select>
                // </div>

            // but in HTML we disabled te aplyala allow kela pahije jevha country select krto tevha lagech state select karay la allow jhala pahije
            citiesListDropDown.disabled = false;
        }

    });

    // select city
    citiesListDropDown.addEventListener("change", async function(){
        const selectedCity = this.value;
        const selectedCountryCode = countriesListDropDown.value;
        // console.log(selectedCity); -> this will gives us selected city 

        // weatherInfo function for selected city
        const weatherInfo = await getWeather(selectedCity, selectedCountryCode);
        // console.log(weatherInfo); ->gives all info of weather in json format 
    
        // calling display weather function 
        displayWeather(weatherInfo);
    
    
    });

});

