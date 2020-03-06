import requests
import zipcodes
"https://automobiles.honda.com/tools/inventory-results/?vehiclemodelseries=clarity-plug-in-hybrid&modelYear=2020&addzipanddealer=true&zipcode=07728"


def main():
    found = {}
    with open('clarity_dealers.txt', 'a+') as f:
        with open('clarity_zips_matches.txt', 'a+') as matches:
            for i in range(1, 100000, 1):
            #for i in range(7700, 7735, 1):
                zipcode = str(i).zfill(5)
                if zipcodes.is_real(zipcode):
                    url = "https://automobiles.honda.com/platform/api/v3/inventoryAndDealers?productDivisionCode=A&modelYear=2020&modelGroup=clarity-plug-in-hybrid&zipCode={}&maxDealers=5&showOnlineRetailingURL=false&preferredDealerId=".format(zipcode)
                    #print(url)
                    #print(zipcode)
                    r = requests.get(url)
                    inv_cnt = len(r.json()['inventory'])
                    if inv_cnt > 0:
                        for n in r.json()['inventory']:
                            dealer_num = n['DealerNumber']
                            for d in r.json()['dealers']:
                                if d['DealerNumber'] == dealer_num:
                                    dealername = d['Name']
                                    dealer_zip_four = d['ZipCode']
                                    save_str = "dealer_zip: {}; dealer: {}, city: {}, state: {}, web: {}, count: {}".format(dealer_zip_four, dealername, d['City'], d['State'], d['WebAddress'], inv_cnt)
                                    if dealer_zip_four not in found.keys():
                                        # we'll miss any dealers where there are two in
                                        # the same zip+4. this should be minimal
                                        found[dealer_zip_four]  = save_str
                                        f.write('%s\n' % save_str)
                                        print("match: {}".format(save_str))
                                    matches.write("%s\n" % zipcode)


if __name__== "__main__":
    main()