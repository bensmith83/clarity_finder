import requests
import zipcodes
import argparse
"https://automobiles.honda.com/tools/inventory-results/?vehiclemodelseries=clarity-plug-in-hybrid&modelYear=2020&addzipanddealer=true&zipcode=07728"


def main():
    parser = argparse.ArgumentParser(description="Query Honda's API to find the elusive Clarity.")
    parser.add_argument('--year', dest='year', action='store', default="2020",
                        help='set the model year to look for')
    args = parser.parse_args()
    modelyear = args.year

    found = {}
    dealer_filename = "{}_clarity_dealers.txt".format(modelyear)
    zips_matches_filename = "{}_clarity_zips_matches.txt".format(modelyear)
    with open(dealer_filename, 'a+') as f:
        with open(zips_matches_filename, 'a+') as matches:
            for i in range(1, 100000, 1):
            #for i in range(7700, 7735, 1):
                zipcode = str(i).zfill(5)
                if zipcodes.is_real(zipcode):
                    url = "https://automobiles.honda.com/platform/api/v3/inventoryAndDealers?productDivisionCode=A&modelYear={}&modelGroup=clarity-plug-in-hybrid&zipCode={}&maxDealers=5&showOnlineRetailingURL=false&preferredDealerId=".format(modelyear,zipcode)
                    #print(url)
                    #print(zipcode)
                    r = requests.get(url)
                    if r.status_code != 200:
                        #print("[*] not zip: {}, status: {}".format(zipcode,r.status_code))
                        continue
                    else:
                        #print("[*] found zip: {}, status: {}".format(zipcode,r.status_code))
                        pass
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