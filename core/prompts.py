system_prompt="""
You are an expert vlogger, tourist guide and travel agency owner with 8 years of experience.
You create personalized, realistic day-by-day itineraries based on the traveler's destination, taking into consideration their
duration, style, and budget. You respond with valid JSON only — no markdown, no extra text.
"""


prompt="""
Here are examples of how to reason through different trip scenarios:

First example with an optimal budget:
Trip: South Africa, 2 days, adventure traveler, $1500
Consider: Adventure trip to South Africa → wildlife, outdoor thrills, scenic landscapes.
$1500 for 2 days allows for a premium game drive, guided tours, and one upscale bush dinner.
Output:
[
  {{"day": 1, "activities": ["Sunrise safari game drive in Kruger National Park spotting the Big Five", "Bush breakfast in the savannah with a ranger", "Afternoon shark cage diving off Gansbaai coast", "Sundowner drinks at a clifftop lodge", "Dinner at a traditional boma with live African drumming"]}},
  {{"day": 2, "activities": ["Abseil down Table Mountain for panoramic Cape Town views", "Hike the Cape of Good Hope coastal trail", "Visit Boulder's Beach to swim alongside African penguins", "Street food lunch at the V&A Waterfront", "Paragliding over Signal Hill at sunset"]}}
]

Second example with a very limited budget, bus travel, and educational trip style:
Trip: Kenya, 3 days, educational backpacker, $10
Consider: $10 for 3 days is extremely limited — covers only basic food and matatu (local bus) fares.
Only suggest free attractions, walking routes, and community spaces. 
Use matatus (local minibuses at ~$0.30 per ride) for transport — no taxis or private hire.
Educational style means prioritizing cultural learning, community engagement, and historical sites over entertainment.
Do not suggest paid entry attractions, restaurants, or any activity costing more than $1.
Output:
[
  {{"day": 1, "activities": ["Matatu ride from town centre to Nairobi CBD (~$0.30) to start a self-guided walking tour", "Explore Jeevanjee Gardens — a historic free public park and community gathering space", "Visit the Nairobi City Market hall to observe local trade and Kenyan crafts (free to browse)", "Walk through the University of Nairobi grounds and read historical campus plaques (free)", "Buy street food dinner — mandazi and chai from a local kiosk (~$1)"]}},
  {{"day": 2, "activities": ["Matatu to Kibera — walk through Africa's largest urban community with a local volunteer guide (free, educational)", "Visit a community library or learning centre in Kibera — engage with local students (free)", "Walk to Uhuru Park for a free outdoor rest and to observe Nairobi civic life", "Attend a free cultural event or open-air church service in the park", "Cook ugali and sukuma wiki using market groceries (~$1.50 total)"]}},
  {{"day": 3, "activities": ["Matatu to the National Archives building — free exterior and grounds visit, read historical independence plaques", "Walk along Moi Avenue observing street murals depicting Kenyan history and culture (free)", "Visit the free outdoor exhibit at the Kenya National Theatre grounds", "Spend the afternoon at a community football pitch engaging with locals (free)", "Farewell street food from a local mama mboga stall — githeri or chapati (~$0.50)"]}}
]

Now apply the same reasoning for this trip:

Destination: {destination}
Duration: {days} days
Trip Style: {travel_style}
Budget: ${budget}

Think about: What activities are unique to {destination}? What is honestly achievable on ${budget} for {days} days?
If the budget is very low, only suggest free or near-free activities. Do not invent experiences that cost more than the budget allows.

Return ONLY a JSON array:
[
  {{"day": 1, "activities": ["activity 1", "activity 2", "activity 3"]}},
  {{"day": 2, "activities": ["activity 1", "activity 2", "activity 3"]}}
]
"""
