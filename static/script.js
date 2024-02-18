
    function showPopup() {
        var popup = document.getElementById('popup-container');
        popup.style.display = 'flex';
    }
    

    function closePopup(e) {
        let popup = document.getElementById(e);
        popup.style.display = 'none';
    }

    //api call
    const apiCall = async (cityName) => {
        let api = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=3ba0e5eedae49070b51c85ad8c30def0&units=metric`;
    
        try {
            const response = await fetch(api);
            
    
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
    
            const json = await response.json();
            console.log(json)
    
            // sunset and sunrise 
            const sunriseTimestamp = json['sys']['sunrise'];
            const sunsetTimestamp = json['sys']['sunset'];
            const sunriseDate = new Date(sunriseTimestamp * 1000);
            const sunsetDate = new Date(sunsetTimestamp * 1000);
            const formatTime = (date) => {
                return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
              };
            const sunriseTime = formatTime(sunriseDate);
            const sunsetTime = formatTime(sunsetDate);
              
            document.getElementById('temp').innerHTML= json['main']['temp']+ "°C";
            document.getElementById('humidity').innerHTML= json['main']['humidity'];
            document.getElementById('wind').innerHTML= json['wind']['speed']+ ", "+ json['wind']['deg'];
            document.getElementById('sun').innerHTML= sunriseTime+  " & "+ sunsetTime;
            console.log('temp' + json['main']['temp'])
            console.log('humidity' + json['main']['humidity'])
    
        } catch (error) {
            console.error('Error fetching data', error);
        }
    };
    

    //function to find city
    function findCity() {
        search = document.querySelector('#search').value;
        
        apiCall(search)
    }


    
            
    
            function findCity() {
                search = document.querySelector('#search').value;
    
                apiCall(search)
            }
    

