/* Config Sample
 *
 * For more information on how you can configure this file
 * see https://docs.magicmirror.builders/configuration/introduction.html
 * and https://docs.magicmirror.builders/modules/configuration.html
 *
 * You can use environment variables using a `config.js.template` file instead of `config.js`
 * which will be converted to `config.js` while starting. For more information
 * see https://docs.magicmirror.builders/configuration/introduction.html#enviromnent-variables
 */
let config = {
	address: "0.0.0.0",	// Address to listen on, can be:
							// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
							// - another specific IPv4/6 to listen on a specific interface
							// - "0.0.0.0", "::" to listen on any interface
							// Default, when address config is left out or empty, is "localhost"
	port: 8080,
	basePath: "/",	// The URL path where MagicMirror² is hosted. If you are using a Reverse proxy
									// you must set the sub path here. basePath must end with a /
 	//ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.0.1/120", "192.168.0.1/24"],
	// ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"],	// Set [] to allow all IP addresses
  	ipWhitelist: [],
									// or add a specific IPv4 of 192.168.1.5 :
									// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
									// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
									// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false,			// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "",	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "",	// HTTPS Certificate path, only require when useHttps is true

	language: "pt",
	locale: "pt-BR",   // this variable is provided as a consistent location
			   // it is currently only used by 3rd party modules. no MagicMirror code uses this value
			   // as we have no usage, we  have no constraints on what this field holds
			   // see https://en.wikipedia.org/wiki/Locale_(computer_software) for the possibilities

	logLevel: ["INFO", "LOG", "WARN", "ERROR"], // Add "DEBUG" for even more logging
	timeFormat: 24,
	units: "metric",

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "Calendário",
			position: "top_left",
			config: {
				calendars: [
					// email etec
					{
						fetchInterval: 60000,
						symbol: "calendar-check",
						url: "https://calendar.google.com/calendar/ical/magicmirror.etec%40gmail.com/public/basic.ics"
					},
					// feriados
					{
						fetchInterval: 60000,
						symbol: "calendar-check",
						url: "https://calendar.google.com/calendar/ical/pt.brazilian%23holiday%40group.v.calendar.google.com/public/basic.ics"
					}
				]
			}
		},
		{
			module: 'MMM-Remote-Control',
			// uncomment the following line to show the URL of the remote control on the mirror
			// position: 'bottom_left',
			// you can hide this module afterwards from the remote control itself
			config: {
				apiKey: 'aa13c710bab642ca843ef59595d6341b'
			}
		},
		{
			module: 'MMM-CustomText',
			position: 'lower_third',
			config: {
				initialMessage: "",
				animationSpeed: 1000 * 2,
			},
		},
		// {
		// 	module: "compliments",
		// 	position: "lower_third",
		// 	config: {
		// 		updateInterval: 1000,
		// 		//compliments: {"anytime" : ["Hello, from config file"]},
		// 		// remoteFileRefreshInterval: 1000,
		// 		// remoteFile: 'http://localhost:5000/compliments.json'
		// 	}
		// },
		{
			module: "weather",
			position: "top_right",
			config: {
				weatherProvider: "openmeteo",
				type: "current",

				// coordenadas da ETEC
				lat: -23.50515420643533,
				lon: -46.65993383440056
			}
		},
		{
			module: "weather",
			position: "top_right",
			header: "Previsão do tempo",
			config: {
				weatherProvider: "openmeteo",
				type: "forecast",
				lat: -23.50515420643533,
				lon: -46.65993383440056
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "Globo: Brasil",
						url: "https://g1.globo.com/rss/g1/brasil/",
						encoding: "UTF-8",
					},
					{
						title: "Globo: Tecnologia e Games",
						url: "https://g1.globo.com/rss/g1/tecnologia/",
						encoding: "UTF-8",
					},
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		},
	]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") { module.exports = config; }
