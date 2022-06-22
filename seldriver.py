import zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def getPlugin(proxy_host, proxy_port, proxy_user, proxy_pass):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (proxy_host, proxy_port, proxy_user, proxy_pass)
    pluginfile = 'proxy_auth_plugin.zip'

    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    
    return pluginfile


def createDriver():
    # us-prime.resdleafproxies.com:7000:cafxyqv24ebyttiw7frq1q+eysY1wIK:mbnuu9xtht
    auth_proxy={
        'proxy_host': 'us-prime.resdleafproxies.com',
        'proxy_port': '7000',
        'proxy_user': 'cafxyqv24ebyttiw7frq1q+eysY1wIK',
        'proxy_pass': 'mbnuu9xtht',
    }

    options = webdriver.ChromeOptions()
    # op
    # 
    # 
    options.add_argument("window-size=1920,1080")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument("--headless") 
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("start-maximized")
    options.add_extension(
        getPlugin(**auth_proxy)
    )
    # driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chromeOptions)
    driver = webdriver.Chrome(options=options)
    
    return driver
    

    # driver.get("http:lumtest.com/myip.json")
    # a = driver.find_element(by=By.TAG_NAME, value="pre")
    # print(a.text)
    # input('Let check the result...')

    # driver.quit()
    
# createDriver()