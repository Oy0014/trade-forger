import requests
from flask import Flask, render_template
from random import randint

class Forge(object):
	def __init__(self, attacker_limiteds: list, victim_limiteds: list, victim_username: str):
		self.forge_data = [
			{
				"ids": attacker_limiteds, 
				"snippet": "", 
				"value": 0
			}, {
				"ids": victim_limiteds, 
				"snippet": "", 
				"value": 0
			}
		]
		self.victim_username = victim_username

		return


	@staticmethod
	def get_lim_info(limited_id: str):
		"""
		Get limited information given limited ID.

		Args:
        	limited_id (int): ID of the limited you want to query information on.

	    Returns:
 	       dict: dictionary cotnaining a respective limited ID's name, RAP, and image url.
		"""

		with requests.Session() as s:
			infoRes = s.get("https://www.rolimons.com/itemapi/itemdetails").json()["items"][limited_id]

			return {
				"name": infoRes[0], 
				"rap": infoRes[2],
				"imageUrl": f"https://images.rbxflip.com/asset-thumbnail/image?assetId={limited_id}&width=150&height=150&format=Png"
			}

	
	def forge_trade_page(self):
		"""
		Generates the HTML for a forged Roblox trade page

	    Returns:
	    	str: HTML content
		"""
		
		with Flask(__name__).app_context():
			for iteration in self.forge_data:
				for lim in [l.strip().lower() for l in iteration["ids"]]:
					a_lim_info = Forge.get_lim_info(lim[1:] if lim.startswith("s") else lim)

					iteration["snippet"] += render_template(
							"forgeTemplates/item_snippet_serial.html" if lim.startswith("s") else "forgeTemplates/item_snippet.html", 
							**{
								"name": a_lim_info["name"], 
								"price": '{:,}'.format(a_lim_info["rap"]),
								"image_url": a_lim_info["imageUrl"],
								"serial": randint(500, 4000)
							}
					)
					iteration["value"] += int(a_lim_info["rap"])

			return render_template("forgeTemplates/main_trade_page.html",
				victim_lim_indicator = self.forge_data[1]["snippet"],
				victim_value_indicator = '{:,}'.format(self.forge_data[1]["value"]),
				attacker_lim_indicator = self.forge_data[0]["snippet"],
				attacker_value_indicator = '{:,}'.format(self.forge_data[0]["value"]),
				victim_username = self.victim_username.strip()
			)