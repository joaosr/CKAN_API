import urllib2
import json
import pprint


def _fetch_package():
    response = urllib2.urlopen('http://demo.ckan.org/api/3/action/package_list')

    assert response.code == 200

    response_dict = json.loads(response.read())

    assert response_dict['success'] is True

    return response_dict['result']

def stat_package():
    result = _fetch_package()
    # pprint.pprint(result)
    print('Published datasets amount: {}'.format(len(result)))




def package_show():
    packages = _fetch_package()
    for i in range(len(packages)):
        url = 'http://demo.ckan.org/api/3/action/package_show?id={}'.format(packages[i])
        package = urllib2.urlopen(url)

        assert package.code == 200

        package_dict = json.loads(package.read())

        assert package_dict['success'] is True

        result = package_dict['result']

        # if len(result['resources']) > 0:
        #     pprint.pprint(package_dict)

        if result['type'] == 'dataset':
            for j in range(len(result['resources'])):
                print(result['resources'][j]['url'])


if __name__ == "__main__":
    stat_package()
    # package_show()



