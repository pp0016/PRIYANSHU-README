Title: Live Content

Description: Fetched live

Source: https://www.apple.com/shop/refurbished/about

---

<!DOCTYPE html>
<html class="en-us amr nojs en seg-consumer us" lang="en-US" >
        <head>


            
    <script crossorigin="anonymous">
        window.ECHO_CONFIG = {
            metadata: {
                environment: "",
                format: "common",
                fmt: "common",
                region: "amr",
                country: "US",
                sf: "us",
                segment: "Consumer",
                locale: "en-us",
                referer: document.referrer,
                node: "standard/home/refurbished/about",
                pageResource: "rs-merch-4",
                feature: "landing",
                targetEnabled: "false"
            },
            config: {
                "pageViewId": Math.random().toString(36).substring(2, 12) + '-' + Date.now().toString(36),
                "app": "com.apple.www.Store",
                "delaySendingPageViewDataMS": 500,
                "altTextEventSampleRatePct": 1.0,
                "interactionEventSampleRatePct": 100.0,
                "resourceEventSampleRatePct": 5.0,
                "rumEventSampleRatePct": 25.0,
                "performanceMeasurePollingIntervalMS": 1000,
                "performanceMeasuresToReport": "".split(','),
                "resourceDisallowedResourceList": "securemetrics.apple.com".split(','),
                "resourcePollingIntervalMS": 2001,
                "sendErrors": true,
                "sendPageViewData": true,
                "sendResourceData":  true,
                "passiveEventIngestionUrl": "https://www.apple.com/fxpmdp/ec/as/v1/api",
                "criticalEventIngestionUrl": "/shop/mdp/api/echo",
                "sendLoggingData": true,
                "eventListeners": null || {},
                "preLoadErrors": []
            }
        };

        window.ECHO_CONFIG.config.preLoadErrorListener =  (event) => {
            window.ECHO_CONFIG.config.preLoadErrors.push(event);
        };

        window.addEventListener('error',window.ECHO_CONFIG.config.preLoadErrorListener);

        window.AS_LOG_LEVEL = "ERROR";
    </script>

                <script crossorigin="anonymous">
                    document.addEventListener('readystatechange', function() {
                        function createAndDispatchEchoEvent(data) {
                            var event = new CustomEvent("echoPerformanceNowEvent", {
                                detail: data,
                            });
                            window.dispatchEvent(event);
                        }

                        if (document.readyState === "interactive") {
                            let lastIntersectedTime = 0;

                            const observerCallback = function (entries, observer) {
                                entries.forEach((entry) => {
                                    if (entry.isIntersecting) {
                                        lastIntersectedTime = performance.now();
                                    }

                                    observer.unobserve(entry.target);
                                });

                                observer.disconnect();

                                // Dispatch time for last intersecting object with viewport
                                createAndDispatchEchoEvent({
                                    id: "viewportLoad",
                                    performanceNow: lastIntersectedTime,
                                });
                            };
                        
                            if (window.IntersectionObserver) {
                                // get all the els on page
                                const itemsInViewport = document.querySelectorAll('*');

                                // instantiate 
                                const intersectionObserver = new IntersectionObserver(observerCallback, {
                                    root: null,
                                    rootMargin: "0px 0px 0px 0px",
                                    threshold: 0.0,
                                });

                                // iterate over all els and observe each one
                                itemsInViewport.forEach(el => {
                                    intersectionObserver.observe(el);
                                });
                            } //END window.IntersectionObserver
                        } //END document.readyState === "interactive"
                    });
                </script>

    <script crossorigin="anonymous">
        (function () {
            const logger = typeof window.Log === "function" ? window.Log("pixel") : window.console;

            try {
                function sanitizeAndNormalizePathname(pathname) {
                    let newPathname = pathname;
                    let decodedPathname;

                    try {
                        decodedPathname = decodeURIComponent(pathname);
                    } catch (error) {
                        decodedPathname = pathname;
                    }

                    // first handle /storepickup and /<sf>/storepickup
                    if (decodedPathname.includes('/storepickup')) {
                        newPathname = '/storepickup';
                    }

                    // then handle /store and /<sf>/store
                    else if (decodedPathname.includes('/store')) {
                        const base = '/store';
                        const path = decodedPathname.split('/store')[1];
                        newPathname = `${base}${path}`;
                    }

                    // handle /search and /<sf>/search
                    else if (decodedPathname.includes('/search')) {
                        newPathname = '/search';
                    }

                    // handle /giftcard and /<sf>/giftcard
                    else if (decodedPathname.includes('/giftcard')) {
                        newPathname = '/giftcard';
                    }

                    // handle /shop/bag/saved_bag and /<sf>/shop/bag/saved_bag
                    else if (decodedPathname.includes('/shop/bag/saved_bag')) {
                        const base = '/shop/bag/saved_bag';
                        newPathname = `${base}`;
                    }

                    // handle /shop/order and /<sf>/shop/order
                    else if (decodedPathname.includes('/shop/bag')) {
                        const base = '/shop/bag';
                        newPathname = `${base}`;
                    }

                    // handle /shop/order and /<sf>/shop/order
                    else if (decodedPathname.includes('/shop/pdpAddToBag')) {
                        const base = '/shop/pdpAddToBag';
                        newPathname = `${base}`;
                    }

                    // handle /shop/order and /<sf>/shop/order
                    else if (decodedPathname.includes('/shop/order')) {
                        const base = '/shop/order';
                        const path = decodedPathname
                            .split(base)[1]
                            .replace(/\d/g, '0')
                            .replace(/[\w.-]+@[\w.-]+\.\w+/g, 'user@example.com');
                        newPathname = `${base}${path}`;
                    }

                    // handle /shop/recap and /<sf>/shop/recap
                    else if (decodedPathname.includes('/shop/recap')) {
                        const base = '/shop/recap';
                        newPathname = `${base}`;
                    }

                    // handle /shop/start and /<sf>/shop/start
                    else if (decodedPathname.includes('/shop/start')) {
                        const base = '/shop/start';
                        newPathname = `${base}`;
                    }

                    // handle /shop/confirm and /<sf>/shop/confirm
                    else if (decodedPathname.includes('/shop/confirm')) {
                        const base = '/shop/confirm';
                        newPathname = `${base}`;
                    }

                    // handle /shop/posThankYou and /<sf>/shop/posThankYou
                    else if (decodedPathname.includes('/shop/posThankYou')) {
                        const base = '/shop/posThankYou';
                        newPathname = `${base}`;
                    }

                    // handle /shop/yoursaves and /<sf>/shop/yoursaves
                    else if (decodedPathname.includes('/shop/yoursaves')) {
                        const base = '/shop/yoursaves';
                        newPathname = `${base}`;
                    }

                    // handle /shop and /<sf>/shop
                    else if (decodedPathname.includes('/shop')) {
                        const base = '/shop';
                        const path = decodedPathname.split('/shop')[1];
                        newPathname = `${base}${path}`;
                    }

                    // handle %
                    if (newPathname.includes('%')) {
                        newPathname = newPathname.split('%')[0];
                    }

                    return newPathname;
                }

                function getSanitizedLocation(location) {
                    if (!location) {
                        return {};
                    }
                    const newLocation = new URL(location);
                    if (newLocation.protocol.startsWith('http')) {
                        return newLocation;
                    }
                    newLocation.pathname = 'pathname';
                    return newLocation;
                }

                function getAosSanitizedLocation(location) {
                    const sanitizedLocation = getSanitizedLocation(location);

                    const normalizedPath = sanitizeAndNormalizePathname(sanitizedLocation.pathname);

                    sanitizedLocation.hash = '';
                    sanitizedLocation.href = `${sanitizedLocation.protocol}//${sanitizedLocation.host}${normalizedPath}`;
                    sanitizedLocation.password = '';
                    sanitizedLocation.pathname = normalizedPath;
                    sanitizedLocation.search = '';

                    return sanitizedLocation;
                }

                const sanitizedLocation = getAosSanitizedLocation(window.location);

                function getPageShopPath(pathname) {
                    let newPathname = pathname;

                    // handle /shop/product and /<sf>/shop/product
                    if (newPathname.includes('/shop/product')) {
                        const base = '/shop/product';
                        newPathname = `${base}`;
                    }

                    const pathElements = newPathname.split('/');

                    if (pathElements.length <= 5) {
                        return newPathname;
                    }

                    return pathElements.slice(0, 4).join('/');
                }

                const { app, pageViewId } = window.ECHO_CONFIG && window.ECHO_CONFIG.config;
                const referrer = document.referrer.includes('apple.com') ? getAosSanitizedLocation(document.referrer).href : document.referrer;
                const host = sanitizedLocation.host;
                const pageHostname = sanitizedLocation.hostname;
                const pagePathname = sanitizedLocation.pathname;
                const pageUrl = sanitizedLocation.href;
                const pageShopPath = getPageShopPath(sanitizedLocation.pathname);
                const recordTime=Date.now();

                function sanitizeQuery({ search, pageResource }) {
                    if ([
                        'accessories-3',
                        'accessories-4',
                        'giftcards-1',
                        'giftcards-3',
                        'ipad-4',
                        'iphone-2',
                        'mac-2',
                        'rs-buyflow-1',
                        'rs-merch-4',
                        'rs-pdp-1',
                        'vision-1',
                        'watch-3',
                    ].includes(pageResource)) {
                        return search
                            .replace(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}/g, 'user@example.com')
                            .replace(/\b[0-9a-f]{40}\b/g, '[REDACTED]');
                    }
                    return '?<query>';
                }

                const pageUrlParams = encodeURIComponent(
                    window.location.search
                    ? sanitizeQuery({ search: window.location.search, pageResource: 'rs-merch-4' })
                    : ''
                );
                const src = `https://www.apple.com/shop/mdp/echo/echo.png?app=${app}&pageViewId=${pageViewId}&recordTime=${recordTime}&referrer=${referrer}&referer=${referrer}&host=${host}&pageHostname=${pageHostname}&pageUrl=${pageUrl}&pagePathname=${pagePathname}&pageShopPath=${pageShopPath}&pageUrlParams=${pageUrlParams}&eventType=pageview&environment=&format=common&region=amr&country=US&sf=us&segment=Consumer&locale=en-us&node=standard/home/refurbished/about&pageResource=rs-merch-4&feature=landing`;
                const pixelScript = document.createElement("img");
                
                pixelScript.setAttribute("src", src);

                const srcB = `https://www.apple.com/fxpmdp/ec/as/v1/echo.png?app=${app}&pageViewId=${pageViewId}&recordTime=${recordTime}&referrer=${referrer}&referer=${referrer}&host=${host}&pageHostname=${pageHostname}&pageUrl=${pageUrl}&pagePathname=${pagePathname}&pageShopPath=${pageShopPath}&pageUrlParams=${pageUrlParams}&eventType=pageview&environment=&format=common&region=amr&country=US&sf=us&segment=Consumer&locale=en-us&node=standard/home/refurbished/about&pageResource=rs-merch-4&feature=landing`;
                const pixelScriptB = document.createElement("img");

                pixelScriptB.setAttribute("src", srcB);
            } catch (e) {
                logger.error(e);
            }
        })();
    </script>

    <noscript>
        <img src="https://www.apple.com/shop/mdp/echo/echo.png?app=com.apple.www.Store&pageViewId=no-js&recordTime=no-js&referrer=no-js&referer=no-js&host=no-js&pageHostname=no-js&pageUrl=no-js&pagePathname=no-js&pageShopPath=no-js&pageUrlParams=no-js&eventType=pageview&environment=&format=common&region=amr&country=US&sf=us&segment=Consumer&locale=en-us&node=standard/home/refurbished/about&pageResource=rs-merch-4&feature=landing" width="1" height="1" />

        <img src="https://www.apple.com/fxpmdp/ec/as/v1/echo.png?app=com.apple.www.Store&pageViewId=no-js&recordTime=no-js&referrer=no-js&referer=no-js&host=no-js&pageHostname=no-js&pageUrl=no-js&pagePathname=no-js&pageShopPath=no-js&pageUrlParams=no-js&eventType=pageview&environment=&format=common&region=amr&country=US&sf=us&segment=Consumer&locale=en-us&node=standard/home/refurbished/about&pageResource=rs-merch-4&feature=landing" width="1" height="1" />
    </noscript>

            <link rel="preconnect" href="https://store.storeimages.cdn-apple.com/4982/store.apple.com" crossorigin="anonymous">
<link rel="dns-prefetch" href="https://store.storeimages.cdn-apple.com/4982/store.apple.com" crossorigin="anonymous">

<link rel="preconnect" href="https://www.apple.com" crossorigin="anonymous">
<link rel="dns-prefetch" href="https://www.apple.com" crossorigin="anonymous">


            <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1" />
    <title>Why Refurbished - Apple</title>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />    
    <meta name="format-detection" content="telephone=no" />        
         <meta name="robots" content="max-image-preview:large" />
        <meta property="og:description" content="Save up to 15% and get a one-year warranty with the Apple Refurbished purchasing program. Read more on the Apple Refurbished promise." />
        <meta property="og:title" content="Why Refurbished" />
        <meta property="og:type" content="website" />
        <meta property="og:image" content="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/og-default?wid=1200&amp;hei=630&amp;fmt=jpeg&amp;qlt=95&amp;.v=1525370171638" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta property="og:site_name" content="Apple" />
        <meta property="og:locale" content="en_US" />
        <meta name="twitter:site" content="@apple" />
        <meta property="og:url" content="https://www.apple.com/shop/refurbished/about" />
    <meta name="description" content="Save up to 15% and get a one-year warranty with the Apple Refurbished purchasing program. Read more on the Apple Refurbished promise." />
        
      
      
      <link rel="canonical" href="https://www.apple.com/shop/refurbished/about" />
          <script  crossorigin="anonymous"> document.cookie = "as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; path=/; domain=apple.com; expires=Fri, 12-Mar-2027 18:31:59 GMT; Secure;"; </script>
			<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":"1","name":"Why Refurbished"}]}</script>
		
		
	<script type="application/json" id="metrics">{"config":{"asMetrics":{"maxCampaignAndAffiliateLength":255,"asMetricsFeatures":["sharedDataLayer"],"dataMule":"v1","storedEntryPointEnabled":false,"graffitiEnabled":false},"omniture":{"account":["applestoreww"],"trackingServer":"securemetrics.apple.com","internalDomains":["store.apple.com","secure.store.apple.com","secure1.store.apple.com","secure2.store.apple.com","epp.apple.com","secure1.epp.apple.com","storeint.apple.com","secure1.storeint.apple.com","www.apple.com"]},"global":{"cookieDomain":"apple.com"}},"data":{"node":"standard/home/refurbished/about","pageName":"AOS: home/refurbished/about","properties":{"isHomePage":false,"encryptedStoreId":"wHF2F2PHCCCX72KDY","serverName":"c868000","characterSetForCountry":"UTF-8","currencyCode":"USD","computedChannel":"AOS: home/refurbished","storeSegmentVariable":"AOS: US Consumer","storeFrontId":"10078","computedCustomStoreName":"AOS: US Consumer","langAttribute":"en-us","evarDataNodesEnabled":true},"currency":"USD","area":"shop"}}</script>
    
    
    

            <script crossorigin="anonymous">
                     if (/(iPad).*OS ([6-9]|[1-9][0-9]).*AppleWebKit.*Mobile.*Safari/.test(navigator.userAgent)) {
                       var headNode = document.getElementsByTagName("head")[0];
var sbNode = document.createElement('meta');
var url = decodeURI("https://www.apple.com/shop/refurbished/about");
var ses = "; " + document.cookie;
var sesParts = ses.split("; s_vi=");
ses = sesParts.length == 2 ? sesParts.pop().split(";").shift() : '';
if (ses !== '') {
    url += url.indexOf('?') >= 0 ? '&' : '?';
    url += 'ses=' + encodeURI(ses);
}
sbNode.name = 'apple-itunes-app';
sbNode.content = 'app-id=375380948, app-argument=' + url;
headNode.appendChild(sbNode);

                     }
                    else if (/(iPhone|iPod).*OS ([6-9]|[1-9][0-9]).*AppleWebKit.*Mobile.*Safari/.test(navigator.userAgent)) {
                      var headNode = document.getElementsByTagName("head")[0];
var sbNode = document.createElement('meta');
var url = decodeURI("https://www.apple.com/shop/refurbished/about");
var ses = "; " + document.cookie;
var sesParts = ses.split("; s_vi=");
ses = sesParts.length == 2 ? sesParts.pop().split(";").shift() : '';
if (ses !== '') {
    url += url.indexOf('?') >= 0 ? '&' : '?';
    url += 'ses=' + encodeURI(ses);
}
sbNode.name = 'apple-itunes-app';
sbNode.content = 'app-id=375380948, app-argument=' + url;
headNode.appendChild(sbNode);

                    }
            </script>



        

        

        

                <script crossorigin="anonymous" type="application/json" id="uiConfig">
        {
                    "fetchHeaders": {
                        "sendHeaders": true
                    }
        }
    </script>

	<script crossorigin="anonymous">
		window.asUnsupportedBrowserUrl = "https://www.apple.com/shop/unsupported";
	</script>


<script crossorigin="anonymous">
	//replace nojs class with js on html element
	(function(html){
		html.className = html.className.replace(/\bnojs\b/,'js')
	})(document.documentElement);

	// add metric shim
	window.s = {
		t: () => {},
		tl: () => {},
		clearVars: () => {},
		pageName: 'disabled',
		disabled: true
	};
</script>

    
            <link data-srs rel="stylesheet" href="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-globalelements-2.25.0-4bbf8/dist/ac-globalnav.css" media="screen, print"  />




        <link data-srs rel="stylesheet" href="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-external-1.74.1-85ac2/dist/us/external.css" media="screen, print"  />
        <link data-srs rel="stylesheet" href="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-vendor-1.36.0-38108/dist/common-css@1.3.3/dist/common.css" media="screen, print"  />
        <link data-srs rel="stylesheet" href="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-merch-4.19.5-d1a23/dist/landing.css" media="screen, print"  />

        <link data-srs rel="stylesheet" href="https://www.apple.com/wss/fonts?families=SF+Pro,v3:200,300,400,500,600|SF+Pro+Icons,v3|Apple+Monochrome+Emoji,v3|Apple+Monochrome+Emoji+Ind,v2|Graphik,v1"  />

    



<link rel="stylesheet" href="https://store.storeimages.cdn-apple.com/4982/store.apple.com/shop/Catalog/global/css/dd/program/refurb.css" media="screen, print" />

	<script crossorigin="anonymous">
		window.irOn=true;
	</script>

    
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-external-1.74.1-85ac2/dist/unsupportedBrowser.min.js"


         nomodule crossorigin="anonymous" integrity="sha384-xA4aSWL+MVd9UwGaciKIe6Ws2in1+cSOXfCZ/KgWWJeJ1eBDhPaftM2S97id4HfU"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-echo-3.35.1-cfadd/dist/echo.min.js"


         async crossorigin="anonymous" type="module" integrity="sha384-0I+kZmpldKJb/SXzAO0FAPzFZfihmidAtr0GGlmveZTTcYctWo5XBEGzXUIBtfDI"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-external-1.74.1-85ac2/dist/external.js"


         crossorigin="anonymous" integrity="sha384-NTbqmRN1XvDxnsUvkcHO9DrZEcmCa3pc4i9dmeOoe4dy6mlL7qVN1D75qRanApEW"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-external-1.74.1-85ac2/dist/log.js"


         crossorigin="anonymous" integrity="sha384-Lpw75dcRr7edu/M8cDUYQwQ1un8+qbzwwYIKToObJpfOn6ojmGE1jjLJG/Hkx2hs"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-vendor-1.36.0-38108/dist/adobe-appmeasurement@3.0.0/third-party/js/ActivityMap.js"


         crossorigin="anonymous" integrity="sha384-1BlDpZz9HnfIFjQdcsaUw/pAX0CahbI4PMPj1Z5XWURAnf0yB/t0e0N67vGRNrOW"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-vendor-1.36.0-38108/dist/adobe-appmeasurement@3.0.0/third-party/js/AppMeasurement.js"


         crossorigin="anonymous" integrity="sha384-jCdgBbxALZsf+8fwj1dHUYG0m12IfDTcySU5niui301KztArcUL2ZqP1I6z1y4u3"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-analytics-1.12.0-54ed8/dist/analytics.js"


         crossorigin="anonymous" integrity="sha384-g/Os09MonGb/qseTfGP1dtTN083Eem3rhig3AqhggOeWMkomzLBz4YPL30xKnYFx"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-vendor-1.36.0-38108/dist/lodash@4.17.21/lodash.min.js"


         crossorigin="anonymous" integrity="sha384-H6KKS1H1WwuERMSm+54dYLzjg0fKqRK5ZRyASdbrI/lwrCc6bXEmtGYr5SwvP1pZ"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-vendor-1.36.0-38108/dist/react-js@19.2.3/dist/react/umd/react.production.min.js"


         crossorigin="anonymous" integrity="sha384-YjP45appJSZ/GgDODJxG9S9NPCwGEl0+bZJyTEO8jMsTfa9q11TPgVIzTqObZo1k"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-vendor-1.36.0-38108/dist/react-js@19.2.3/dist/react-dom/umd/react-dom.production.min.js"


         crossorigin="anonymous" integrity="sha384-2hK6/EYXuQi8/C+gVN5OuxSDAAqSYnnBT+TY2TdShtHdYe55fr2MF3xOND6NJ+ar"></script>
        <script data-srs

            src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-merch-4.19.5-d1a23/dist/landing.js"


         crossorigin="anonymous"></script>

        <script data-srs src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-globalelements-2.25.0-4bbf8/dist/ac-globalnav.umd.js" defer crossorigin="anonymous" integrity="sha384-3QnQXRcOP6ItGTJ9lbKxojuy9pV1KAEykS7ix0Te+k7wj5b42Rcj0eLpLDTNxBH5"></script>
    <script data-srs src="https://store.storeimages.cdn-apple.com/4982/store.apple.com/static-resources/rs-globalelements-2.25.0-4bbf8/dist/globalelements.js" crossorigin="anonymous" integrity="sha384-Vd4M0TI5DAjH73dnM/hI4oN/2/mxN9SrrUwWVLjAtD3r4q5hE2DcNVMnjkwpAinh"></script>








    


        <script id="shldVerify" type="module" crossorigin="anonymous" src="/shop/shld/v2_1/verify.js" integrity="sha384-d7DL6Ye+MzFxtO0ROXGGLkTMUIfon4U+xqJ2gxJCkMMJdE9ZjkkgG/3JcY6tl3RP"></script>
        <script crossorigin="anonymous">
            window.shldConfig= {
                isEnabled: true
            };
        </script>







        

            <script crossorigin="anonymous">
    window.chatConfig = {"chat":{"page":[{"name":"WEB_CHAT_COUNTRY","value":"us"},{"name":"WEB_CHAT_LANGUAGE","value":"en"},{"name":"WEB_CHAT_ORDERNUMBER","value":null},{"name":"WEB_CHAT_GEO","value":"amr"},{"name":"WEB_CHAT_SEGMENT","value":"consumer"},{"name":"WEB_CHAT_SECTION","value":"product selection"},{"name":"WEB_CHAT_SUBSECTION","value":"about"},{"name":"WEB_CHAT_REFER","value":"https://www.google.com/"},{"name":"WEB_CHAT_APP","value":"AOS"},{"name":"WEB_CHAT_PAGE","value":"AOS: home/refurbished/about"},{"name":"url","value":"https://contactretail.apple.com"}]}};
</script>



    

<script crossorigin="anonymous">
	if(!/dssid2/.test(document.cookie) || !/as_dc/.test(document.cookie)) {
		document.addEventListener('DOMContentLoaded', () => {
			const ie = document.createElement("IMG");
			ie.src = '/shop/dc';
			ie.width = 1;
			ie.height = 1;
			ie.style.display = "none";
			ie.alt = "";
			document.body.appendChild(ie);
		});
	}
</script>


    


</head>


    <body class="as-theme-light-heroimage">
        	<script crossorigin="anonymous">
		window.as = window.as || {};
		window.as.isFlex = true;
	</script>
            <div class="metrics">
            <noscript>
        <img src="https://securemetrics.apple.com/b/ss/applestoreww/1/H.8--NS/0?pageName=No-Script:AOS%3A+home%2Frefurbished%2Fabout" height="1" width="1" alt=""/>
    </noscript>


        
        	<script></script>


        
        
    <script crossorigin="anonymous">
            if (window.asMetrics && window.asMetrics.initialize) {
                window.asMetrics.initialize();
            }
    </script>


    </div>




<script crossorigin="anonymous">
	if(!/dssid2/.test(document.cookie) || !/as_dc/.test(document.cookie)) {
		document.addEventListener('DOMContentLoaded', () => {
			const ie = document.createElement("IMG");
			ie.src = '/shop/dc';
			ie.width = 1;
			ie.height = 1;
			ie.style.display = "none";
			ie.alt = "";
			document.body.appendChild(ie);
		});
	}
</script>




        
        
        

        <div id="page">

            


    <script id="aos-gn-links" type="application/json">
    {  "educationrouting" : "https://www.apple.com/shop/browse/home/education_routing",  "special_deals" : "https://www.apple.com/shop/refurbished",  "buy_iphone/iphone_se" : "https://www.apple.com/iphone",  "buy_mac" : "https://www.apple.com/shop/buy-mac",  "edu_store" : "https://www.apple.com/us-edu/store",  "order/list" : "https://secure.store.apple.com/shop/order/list",  "buy_airtag/airtag" : "https://www.apple.com/shop/browse/home/shop_airtag/family/airtag",  "buy_watch" : "https://www.apple.com/shop/buy-watch",  "ipad/keyboards" : "https://www.apple.com/shop/ipad/accessories/keyboards",  "ipad/accessories" : "https://www.apple.com/shop/ipad/accessories",  "accessories/all_accessories/made_by_apple" : "https://www.apple.com/shop/accessories/all/made-by-apple",  "watch/bands" : "https://www.apple.com/shop/watch/bands",  "buy_homepod/homepod_mini" : "https://www.apple.com/shop/homepod/family/homepod-mini",  "eppstore/veteransandmilitary" : "https://www.apple.com/shop/browse/home/veterans_military",  "studio/apple_watch" : "https://www.apple.com/shop/studio/apple-watch",  "payment_plan" : "https://www.apple.com/shop/browse/finance/instant_credit",  "buy_homepod/homepod" : "https://www.apple.com/shop/homepod/family/homepod",  "buy_tv/apple_tv_4k" : "https://www.apple.com/shop/tv/family/apple-tv-4k",  "trade_in" : "https://www.apple.com/shop/trade-in",  "mac/accessories" : "https://www.apple.com/shop/mac/accessories",  "accessories/all_accessories/beats_featured" : "https://www.apple.com/shop/beats/accessories",  "buy_iphone/carrier_offers" : "https://www.apple.com/shop/buy-iphone/carrier-offers",  "store" : "https://www.apple.com/store",  "watch/accessories" : "https://www.apple.com/shop/watch/accessories",  "buy_ipad" : "https://www.apple.com/shop/buy-ipad",  "buy_iphone" : "https://www.apple.com/shop/buy-iphone",  "smart_home/accessories" : "https://www.apple.com/shop/smart-home/accessories",  "buy_iphone/iphone_12" : "https://www.apple.com/iphone",  "buy_iphone/iphone_13" : "https://www.apple.com/iphone",  "product/MW5G3" : "/shop/product/mw5g3am/a/siri-remote",  "iphone/accessories" : "https://www.apple.com/shop/iphone/accessories",  "buy_accessories" : "https://www.apple.com/shop/accessories/all"}
    </script>


            <meta name="aos-gn-template" content="2.24.0 - Fri Jun 19 2026 08:45:23 GMT-0700 (Pacific Daylight Time)" />
            <meta name="globalnav-store-key" content="SJHJUH4YFCTTPD4F4" />
            <meta name="globalnav-search-field[action]" content="/search" />
            <meta name="globalnav-submenus-enabled" content="true" data-ff-enabled data-cms />
                <meta name="globalmessage-segment-redirect" content="true" data-cms />
            <meta name="globalnav-search-suggestions-enabled" content="true" data-cms />
            <meta name="globalnav-bag-flyout-enabled" content="true" data-cms />































<div id="globalheader">
  <aside id="globalmessage-segment" lang="en-US" dir="ltr" class="globalmessage-segment">
    <ul data-strings="{&quot;view&quot;:&quot;{%STOREFRONT%} Store Home&quot;,&quot;segments&quot;:{&quot;smb&quot;:&quot;Business Store Home&quot;,&quot;eduInd&quot;:&quot;Education Store Home&quot;,&quot;other&quot;:&quot;Store Home&quot;},&quot;exit&quot;:&quot;Exit&quot;}" class="globalmessage-segment-content"></ul>
  </aside>
  <nav id="globalnav" lang="en-US" dir="ltr" aria-label="Global" data-analytics-element-engagement-start="globalnav:onFlyoutOpen" data-analytics-element-engagement-end="globalnav:onFlyoutClose" data-store-api="https://www.apple.com/shop/bag/status" data-analytics-activitymap-region-id="global nav" data-analytics-region="global nav" class="globalnav no-js">
    <div class="globalnav-content">
      <div class="globalnav-item globalnav-menuback">
        <button aria-label="Main menu" class="globalnav-menuback-button">
          <span aria-hidden="true" class="globalnav-chevron-icon"><svg height="48" viewbox="0 0 9 48" width="9" xmlns="http://www.w3.org/2000/svg">
              <path d="m1.5618 24.0621 6.5581-6.4238c.2368-.2319.2407-.6118.0088-.8486-.2324-.2373-.6123-.2407-.8486-.0088l-7 6.8569c-.1157.1138-.1807.2695-.1802.4316.001.1621.0674.3174.1846.4297l7 6.7241c.1162.1118.2661.1675.4155.1675.1577 0 .3149-.062.4326-.1846.2295-.2388.2222-.6187-.0171-.8481z"></path></svg></span>
        </button>
      </div>
      <ul id="globalnav-list" role="none" class="globalnav-list">
        <li data-analytics-element-engagement="globalnav hover - apple" class="globalnav-item globalnav-item-apple">
          <a href="https://www.apple.com/" data-globalnav-item-name="apple" data-analytics-title="apple home" aria-label="Apple" class="globalnav-link globalnav-link-apple" data-autom="gn_apple"><span aria-hidden="true" class="globalnav-image-regular globalnav-link-image"><svg height="44" viewbox="0 0 14 44" width="14" xmlns="http://www.w3.org/2000/svg">
                <path d="m13.0729 17.6825a3.61 3.61 0 0 0 -1.7248 3.0365 3.5132 3.5132 0 0 0 2.1379 3.2223 8.394 8.394 0 0 1 -1.0948 2.2618c-.6816.9812-1.3943 1.9623-2.4787 1.9623s-1.3633-.63-2.613-.63c-1.2187 0-1.6525.6507-2.644.6507s-1.6834-.9089-2.4787-2.0243a9.7842 9.7842 0 0 1 -1.6628-5.2776c0-3.0984 2.014-4.7405 3.9969-4.7405 1.0535 0 1.9314.6919 2.5924.6919.63 0 1.6112-.7333 2.8092-.7333a3.7579 3.7579 0 0 1 3.1604 1.5802zm-3.7284-2.8918a3.5615 3.5615 0 0 0 .8469-2.22 1.5353 1.5353 0 0 0 -.031-.32 3.5686 3.5686 0 0 0 -2.3445 1.2084 3.4629 3.4629 0 0 0 -.8779 2.1585 1.419 1.419 0 0 0 .031.2892 1.19 1.19 0 0 0 .2169.0207 3.0935 3.0935 0 0 0 2.1586-1.1368z"></path></svg></span><span aria-hidden="true" class="globalnav-image-compact globalnav-link-image"><svg height="48" viewbox="0 0 17 48" width="17" xmlns="http://www.w3.org/2000/svg">
                <path d="m15.5752 19.0792a4.2055 4.2055 0 0 0 -2.01 3.5376 4.0931 4.0931 0 0 0 2.4908 3.7542 9.7779 9.7779 0 0 1 -1.2755 2.6351c-.7941 1.1431-1.6244 2.2862-2.8878 2.2862s-1.5883-.734-3.0443-.734c-1.42 0-1.9252.7581-3.08.7581s-1.9611-1.0589-2.8876-2.3584a11.3987 11.3987 0 0 1 -1.9373-6.1487c0-3.61 2.3464-5.523 4.6566-5.523 1.2274 0 2.25.8062 3.02.8062.734 0 1.8771-.8543 3.2729-.8543a4.3778 4.3778 0 0 1 3.6822 1.841zm-6.8586-2.0456a1.3865 1.3865 0 0 1 -.2527-.024 1.6557 1.6557 0 0 1 -.0361-.337 4.0341 4.0341 0 0 1 1.0228-2.5148 4.1571 4.1571 0 0 1 2.7314-1.4078 1.7815 1.7815 0 0 1 .0361.373 4.1487 4.1487 0 0 1 -.9867 2.587 3.6039 3.6039 0 0 1 -2.5148 1.3236z"></path></svg></span><span class="globalnav-link-text">Apple</span></a>
        </li>
        <li data-topnav-flyout-item="menu" data-topnav-flyout-label="Menu" role="none" class="globalnav-item globalnav-menu">
          <div data-topnav-flyout="menu" class="globalnav-flyout">
            <div class="globalnav-menu-list">
              <div data-analytics-element-engagement="globalnav hover - store" class="globalnav-item globalnav-item-store globalnav-item-menu">
                <ul role="none" class="globalnav-submenu-trigger-group">
                  <li class="globalnav-submenu-trigger-item">
                    <a href="/store" data-globalnav-item-name="store" data-topnav-flyout-trigger-compact="true" data-analytics-title="store" data-analytics-element-engagement="hover - store" aria-label="Store" class="globalnav-link globalnav-submenu-trigger-link globalnav-link-store" data-autom="gn_store"><span class="globalnav-link-text-container"><span aria-hidden="true" class="globalnav-image-regular globalnav-link-image"><svg height="44" viewbox="0 0 30 44" width="30" xmlns="http://www.w3.org/2000/svg">
                            <path d="m26.5679 20.4629c1.002 0 1.67.738 1.693 1.857h-3.48c.076-1.119.779-1.857 1.787-1.857zm2.754 2.672v-.387c0-1.963-1.037-3.176-2.742-3.176-1.735 0-2.848 1.289-2.848 3.276 0 1.998 1.096 3.263 2.848 3.263 1.383 0 2.367-.668 2.66-1.746h-1.008c-.264.557-.814.856-1.629.856-1.072 0-1.769-.791-1.822-2.039v-.047zm-9.547-3.451h.96v.937h.094c.188-.615.914-1.049 1.752-1.049.164 0 .375.012.504.03v1.007c-.082-.023-.445-.058-.644-.058-.961 0-1.659 1.098-1.659 1.535v3.914h-1.007zm-4.27 5.519c-1.195 0-1.869-.867-1.869-2.361 0-1.5.674-2.361 1.869-2.361 1.196 0 1.87.861 1.87 2.361 0 1.494-.674 2.361-1.87 2.361zm0-5.631c-1.798 0-2.912 1.237-2.912 3.27 0 2.027 1.114 3.269 2.912 3.269 1.799 0 2.913-1.242 2.913-3.269 0-2.033-1.114-3.27-2.913-3.27zm-5.478-1.475v1.635h1.407v.843h-1.407v3.575c0 .744.282 1.06.938 1.06.182 0 .281-.006.469-.023v.849c-.199.035-.393.059-.592.059-1.301 0-1.822-.481-1.822-1.688v-3.832h-1.02v-.843h1.02v-1.635zm-8.103 5.694c.129.885.973 1.447 2.174 1.447 1.137 0 1.975-.615 1.975-1.453 0-.72-.527-1.177-1.693-1.47l-1.084-.282c-1.53-.386-2.192-1.078-2.192-2.279 0-1.436 1.201-2.408 2.988-2.408 1.635 0 2.854.972 2.942 2.338h-1.061c-.146-.867-.861-1.383-1.916-1.383-1.125 0-1.869.562-1.869 1.418 0 .662.463 1.043 1.629 1.342l.885.234c1.752.439 2.455 1.119 2.455 2.361 0 1.553-1.225 2.543-3.158 2.543-1.793 0-3.03-.949-3.141-2.408z"></path></svg></span><span class="globalnav-link-text">Store</span></span></a>
                  </li>
                </ul>
              </div>
              <div data-analytics-element-engagement="globalnav hover - mac" class="globalnav-item globalnav-item-mac globalnav-item-menu">
                <ul role="none" class="globalnav-submenu-trigger-group">
                  <li class="globalnav-submenu-trigger-item">
                    <a href="https://www.apple.com/mac/" data-globalnav-item-name="mac" data-topnav-flyout-trigger-compact="true" data-analytics-title="mac" data-analytics-element-engagement="hover - mac" aria-label="Mac" class="globalnav-link globalnav-submenu-trigger-link globalnav-link-mac" data-autom="gn_mac"><span class="globalnav-link-text-container"><span aria-hidden="true" class="globalnav-image-regular globalnav-link-image"><svg height="44" viewbox="0 0 23 44" width="23" xmlns="http://www.w3.org/2000/svg">
                            <path d="m8.1558 25.9987v-6.457h-.0703l-2.666 6.457h-.8907l-2.666-6.457h-.0703v6.457h-.9844v-8.4551h1.2246l2.8945 7.0547h.0938l2.8945-7.0547h1.2246v8.4551zm2.5166-1.7696c0-1.1309.832-1.7812 2.3027-1.8691l1.8223-.1113v-.5742c0-.7793-.4863-1.207-1.4297-1.207-.7559 0-1.2832.2871-1.4238.7852h-1.0195c.1348-1.0137 1.1309-1.6816 2.4785-1.6816 1.541 0 2.4023.791 2.4023 2.1035v4.3242h-.9609v-.9318h-.0938c-.4102.6738-1.1016 1.043-1.9453 1.043-1.2246 0-2.1328-.7266-2.1328-1.8809zm4.125-.5859v-.5801l-1.6992.1113c-.9609.0645-1.3828.

