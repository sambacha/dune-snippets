import requests
from time import sleep
import json
import tqdm

GNOSIS_ACCOUNT_COOKIE = "4837-1810fc3e62122c19ba4de7bf07428e5d|8f17242444d80d6cf1881b3accc8c4f5227004b53c66d84a13d795dcd8a811daca56766e66a5849e768d547f866a6dda816e1f7ad3468d962f5037c4126e39ba"


class DuneServerError(Exception):
    pass


def run_dune_query_helper(
    query_id, query_parameters, remember_token_cookie=GNOSIS_ACCOUNT_COOKIE
):
    payload = {"id": query_id, "parameters": query_parameters, "max_age": 0}

    headers = {"content-type": "application/json", "accept": "application/json"}

    jar = requests.cookies.RequestsCookieJar()

    # TODO: get this cookie somehow (otherwise just paste it from the browser after authentication)
    jar.set(
        "remember_token",
        remember_token_cookie,
        domain="explore.duneanalytics.com",
        path="/",
    )

    # Send query
    r = requests.post(
        f"https://explore.duneanalytics.com/api/queries/{query_id}/results",
        json=payload,
        headers=headers,
        cookies=jar,
    )
    if r.status_code != 200:
        raise DuneServerError(r.text)
    j = r.json()
    if "job" not in j.keys():
        raise DuneServerError(r.text)
    job = j["job"]

    # Wait for job completion
    while job["query_result_id"] is None:
        r = requests.get(
            f"https://explore.duneanalytics.com/api/jobs/{job['id']}",
            headers=headers,
            cookies=jar,
        )
        if r.status_code != 200:
            raise DuneServerError(r.text)
        j = r.json()
        if "job" not in j.keys():
            raise DuneServerError(r.text)
        job = j["job"]
        sleep(3)

    # Get results
    query_result_id = job["query_result_id"]
    r = requests.get(
        f"https://explore.duneanalytics.com/api/query_results/{query_result_id}",
        headers=headers,
        cookies=jar,
    )
    return r.json()


def run_dune_query(
    query_id, query_parameters, remember_token_cookie=GNOSIS_ACCOUNT_COOKIE
):
    wait_time = 5
    backoff_factor = 2
    while True:
        try:
            return run_dune_query_helper(
                query_id, query_parameters, remember_token_cookie
            )
        except DuneServerError as e:
            print(f"Dune server error: {e}. Retrying in {wait_time} secs.")
            sleep(wait_time)
            wait_time *= backoff_factor


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Dune Analytics query.")

    parser.add_argument("query_id", type=int, help="Query id.")

    parser.add_argument(
        "--auth_cookie",
        type=str,
        default=GNOSIS_ACCOUNT_COOKIE,
        help='Contents of "remember_token" cookie (get it from a browser after authenticating)',
    )

    parser.add_argument(
        "--query_parameters",
        type=str,
        nargs="*",
        help="Query parameters, in the form of par1=value1, par2=value2",
    )

    args = parser.parse_args()

    parameters = {kv.split("=")[0]: kv.split("=")[1] for kv in args.query_parameters}

    """
    output = run_dune_query(args.query_id, parameters, args.auth_cookie)
    print(json.dumps(output, indent=4))

    #query_id = 9536
    #query_parameters = {"from_block":"11138424","to_block":"11138430"}
    auth_cookie = "4837-1810fc3e62122c19ba4de7bf07428e5d|8f17242444d80d6cf1881b3accc8c4f5227004b53c66d84a13d795dcd8a811daca56766e66a5849e768d547f866a6dda816e1f7ad3468d962f5037c4126e39ba"

    def write_csv(filename, data_dicts):
        import csv
        with open(filename, 'w+', newline='') as csvfile:
            fieldnames = ['block_number', 'index', 'sell_amount', 'buy_amount', 'path', 'output_amounts', 'block_time', 'address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_dicts)

    step = 6646

    all_output=[]
    for b in tqdm.tqdm(range(11827625, 11874148, step)):
        output = run_dune_query(9536, {"from_block":str(b),"to_block":str(b+step)}, auth_cookie)
        print(output)
        all_output += output['query_result']['data']['rows']
        write_csv("out.csv", all_output)
    """
