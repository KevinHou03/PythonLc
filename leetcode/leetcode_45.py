def jump(nums):
    result = 0
    start = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if farthest > len(nums) - 1:
            result += 1
            break
        if i == start:
            start = farthest
            result += 1
    return result
'''
Encomium for Guatemala

Located in the beautiful central America, bordered by the turquoise blue south Pacific Ocean and the Caribbean Sea, Guatemala is an exquisite and breathtaking canvas that unfolds and amazes the world. The friendly Mayans have survived for centuries in this fertile land long nourished by volcanoes and tropical currents, creating an enriched tradition of sculpture and architectural mastery while spreading to the world cultures and fruits that are distinctive to the region, including Jocote and Zapote.

When the truth is covered by appearances, controversy and misunderstanding are unavoidable, and the cocoon of information has dumbed down people's ability to access what they deserve to know. Guatemala is like a glamorous woman, but her mesmerizing face is firmly covered by a black veil, so the world can't see her true nature.

The country is perceived as having very poor facilities, with mosquitoes infesting muddy and low brick buildings and children playing naked in the streets. What is overlooked is the country's commitment to environmental protection and the unforgettable pulchritude that can be found in any corner of the country, whether in the center of the Guatemala City or on the dirt roads of the villages like San Huan La Laguna.

Lake Atitlan, a tear of Aphrodite, and the precious of San Pedro, has the most crystal clear water near the equator region, through whose one can see her gigantic guardians — Volcano SanPedro, Toliman, and Atitlan — standing in the rolling hills of the lake. As tourists paddle in the lake, they sink into the waves, the mountains, and the quiet sea of clouds.

The word “fuego” means “fire” in Spanish, and, beside this, there is no better name for a 4000-meter volcano that erupts every 10 - 20 minutes. Volcano Fuego, together with other 37 volcanos, among which 3 are highly active, endowed Guatemala with a tenacious and unceasing vitality. Hundreds of thousands of tourists adventure to Fuego every year during the dry season of Antigua city which has beholden the power of this god of fire for three hundred years. They bravely climbed 4,000 meters just to catch a glimpse of his majesty. When the sun comes down, Fuego spews tens of meters of lava that lights up the city like stars falling from the sky to earth and volcanic ash hangs around the summit of the mountain. The whole country trembles under his roar, a thrilling symphony (Nocturne?) at night.

You are regretfully mistaken if you think Guatemala is all about nature. 

People also denounce this land by its high crime rate, and this is actually the truth. However, there are very few nice places in the world if that's a reason for people to categorize it as a crappy place. The capital, Guatemala City, has several blocks that have high murder rate, and so does San Francisco,  Los Angeles, Chicago, and, perhaps, New York. Even so, they are among the greatest cities in the world. Every country and Every place has unpleasant people that are constantly causing troubles, and we shouldn't be full of prejudice on this issue.

Guatemalans are friendly people. They are mostly devout Catholics. The unemployment rate in Guatemala is surprisingly 3.5%, lower than that of Singapore, Netherland, UK, and it is decreasing annually. In the city you can see people smiling at you while they are busy at their jobs: carrying luggages, riding motorcycle, and taking care of their baby. They play music and sing their songs at night when they are done with their daily business. I can see that they enjoy their music, but they usually sing quietly, like an Acappella with a guitar.


The industry and diligence of Guatemalans have also created countless kinds of local products, like the food. Thousands of years of traditional cooking history, combined with the culture incorporated during the colonial era, have brought this country its unique cuisine. Pepian de pollo, a dish that is always praised, has successfully captured my heart and whetted my appetite after a tiring hike and I devoured it! The local food is extensively locally sourced, utilizing the flavors of berries, fruits, and even chocolate to give visitors' taste buds something they've never experienced before.

When it comes to Guatemala’s specialties, one of the topics that never escapes us is coffee. During the long process of formation, eruption and death of the volcano, which lasted for tens of thousands of years, the soil was infiltrated with nutrients from the volcano for a long period of time, resulting in a unique environment conducive to the flavor of coffee beans. Any coffee lover will be attracted by the unique combination of smoky and sweet fruity flavor of Guatemalan coffee. The special geography of the area gives the coffee a distinctive layered with each having different taste.







'''



