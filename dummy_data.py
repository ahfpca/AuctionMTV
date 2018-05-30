from apps.login_reg.models import *
from apps.auction.models import *

#Categories: Food, Drink, CellPhone, Laptop, Clothing, Electronics, Homeware, Furniture, Skincare, Other


# User.objects.create(user_uniq = "$2b$12$k4UqOJRqNVa8gELP64IPVOXFxBshK.JUXHrTOPnAJHX62WIOgCb4G", first_name = "Theresa", last_name = "Eliger", email = "theresa@gmail.com", passcode = "$2b$12$oy5mjh6uBMZNn6AVdxb/6e.5uZuVW/qsAb1Fnhv/SvDpCG0bYDBPS", created_at = "2018-05-30 18:57:42.419699", updated_at = "2018-05-30 18:57:42.702240")
# User.objects.create(user_uniq = "$2b$12$TnLka2nraMKubsrj.Nv/BuL9/9IPf/z7HZiCwcyghT8JG6egZevU2", first_name = "Arash", last_name = "HF", email = "ahfpca@gmail.com", passcode = "$2b$12$9v6OrU0CuSyMFCio4b.tKedimz73bAfEXGtL3aOFkkzQriPZabWJi", created_at = "2018-05-30 19:49:12.241780", updated_at = "2018-05-30 19:49:12.536627")
# User.objects.create(user_uniq = "$2b$12$9Ua0hPy6w6o8vyJqyht0oudW0M5w65d93Rq7n70oeFRuUHHvxRPwS", first_name = "Scott", last_name = "Olson", email = "scott@gmail.com", passcode = "$2b$12$Mv9XdDt48GJiXeT4/gn4yuNU2uIjuaNvho7KqJcOZ7uokx0d0sK9y", created_at = "2018-05-30 19:50:45.109643", updated_at = "2018-05-30 19:50:45.399371")
# User.objects.create(user_uniq = "$2b$12$.r0GQVcHJ3ig3GYwvl0VeuHpdBiJ/fFQxBYculZ2u3ihAHGHVxUI2", first_name = "Erik", last_name = "Nordland", email = "erik@gmail.com", passcode = "$2b$12$wYOSSTh5aX6fxiftWU2nAejxDy8pQ.L1Ybnc43/vAR.Qj9MAh9boC", created_at = "2018-05-30 19:51:52.703945", updated_at = "2018-05-30 19:51:52.991519")


Category.objects.create(category_name = "Food")
Category.objects.create(category_name = "Drink")
Category.objects.create(category_name = "Cellphone")
Category.objects.create(category_name = "Laptop")
Category.objects.create(category_name = "Clothing")
Category.objects.create(category_name = "Electronics")
Category.objects.create(category_name = "Homeware")
Category.objects.create(category_name = "Furniture")
Category.objects.create(category_name = "Skincare")
Category.objects.create(category_name = "Car")
Category.objects.create(category_name = "Other")

Genre.objects.create(genre_name = "Action")
Genre.objects.create(genre_name = "Adventure")
Genre.objects.create(genre_name = "Animated")
Genre.objects.create(genre_name = "Comedy")
Genre.objects.create(genre_name = "Drama")
Genre.objects.create(genre_name = "Fantasy")
Genre.objects.create(genre_name = "Family")
Genre.objects.create(genre_name = "Horror")
Genre.objects.create(genre_name = "Mystery")
Genre.objects.create(genre_name = "Romance")
Genre.objects.create(genre_name = "Sci-Fi")


g1 = Genre.objects.filter(genre_name = "Action").first()
g2 = Genre.objects.filter(genre_name = "Comedy").first()
g3 = Genre.objects.filter(genre_name = "Horror").first()
g4 = Genre.objects.filter(genre_name = "Family").first()
g5 = Genre.objects.filter(genre_name = "Drama").first()

u1 = User.objects.filter(first_name = "Theresa").first()
u2 = User.objects.filter(first_name = "Arash").first()
u3 = User.objects.filter(first_name = "Scott").first()
u4 = User.objects.filter(first_name = "Erik").first()

c1 = Category.objects.filter(category_name = "Drink").first()
c2 = Category.objects.filter(category_name = "Cellphone").first()
c3 = Category.objects.filter(category_name = "Laptop").first()
c4 = Category.objects.filter(category_name = "Clothing").first()
c5 = Category.objects.filter(category_name = "Food").first()
c6 = Category.objects.filter(category_name = "Car").first()


# Movies
Media.objects.create(media_title = "Avengers: Infinite War", release_year = 2018, media_type = 1, fk_genre = g1, fk_user = u1)
Media.objects.create(media_title = "It", release_year = 2018, media_type = 1, fk_genre = g3, fk_user = u4)
Media.objects.create(media_title = "Dumb and Dumber 3", release_year = 2019, media_type = 1, fk_genre = g2, fk_user = u1)
Media.objects.create(media_title = "Daddy's Home 3", release_year = 2019, media_type = 1, fk_genre = g4, fk_user = u2)

# TV series
Media.objects.create(media_title = "Blacklist - S7", release_year = 2019, media_type = 2, fk_genre = g1, fk_user = u1)
Media.objects.create(media_title = "Supernatural - S14", release_year = 2019, media_type = 2, fk_genre = g3, fk_user = u2)
Media.objects.create(media_title = "Modern Family - S6", release_year = 2019, media_type = 2, fk_genre = g4, fk_user = u3)
Media.objects.create(media_title = "Stranger Things - S4", release_year = 2019, media_type = 2, fk_genre = g3, fk_user = u4)
Media.objects.create(media_title = "Minhunter - S3", release_year = 2019, media_type = 2, fk_genre = g5, fk_user = u1)
Media.objects.create(media_title = "Better Call Saul - S5", release_year = 2019, media_type = 2, fk_genre = g5, fk_user = u3)

m4 = Media.objects.filter(media_id = 4).first()
m5 = Media.objects.filter(media_id = 5).first()



Auction.objects.create(title = "Drinks in Blacklist - S7", description = "Actors drink soda in 4 episodes.", duration_seconds = 20, starting_bid = 2000, current_bid = 3400, deadline = "2018-06-10 20:00:00", fk_category = c1, fk_user = u1, fk_media = m5)
Auction.objects.create(title = "Clothing in Blacklist - S7", description = "Actor wears suite and there are 3 times referring to the brand to the suite.", duration_seconds = 15, starting_bid = 10000, current_bid = 31000, deadline = "2018-06-10 20:00:00", fk_category = c4, fk_user = u1, fk_media = m5)
Auction.objects.create(title = "Cars in Daddy's Home 3", description = "There is two long carchasing scenes.", duration_seconds = 120, starting_bid = 20000, current_bid = 53000, deadline = "2018-06-25 10:00:00", fk_category = c6, fk_user = u2, fk_media = m4)
Auction.objects.create(title = "Drinks in Daddy's Home 3", description = "Actors drink in 4 scenes", duration_seconds = 12, starting_bid = 3000, current_bid = 6400, deadline = "2018-06-25 10:00:00", fk_category = c1, fk_user = u2, fk_media = m4)

a1 = Auction.objects.filter(auction_id = 1).first()
a2 = Auction.objects.filter(auction_id = 2).first()
a3 = Auction.objects.filter(auction_id = 3).first()
a4 = Auction.objects.filter(auction_id = 4).first()


# Auction 1
Bid.objects.create(bid_amount = 2100, fk_auction = a1, fk_user = u2)
Bid.objects.create(bid_amount = 2400, fk_auction = a1, fk_user = u3)
Bid.objects.create(bid_amount = 2500, fk_auction = a1, fk_user = u2)
Bid.objects.create(bid_amount = 3000, fk_auction = a1, fk_user = u4)
Bid.objects.create(bid_amount = 3200, fk_auction = a1, fk_user = u3)
Bid.objects.create(bid_amount = 3400, fk_auction = a1, fk_user = u2)

# Auction 2
Bid.objects.create(bid_amount = 10000, fk_auction = a2, fk_user = u2)
Bid.objects.create(bid_amount = 12000, fk_auction = a2, fk_user = u3)
Bid.objects.create(bid_amount = 18000, fk_auction = a2, fk_user = u2)
Bid.objects.create(bid_amount = 19000, fk_auction = a2, fk_user = u4)
Bid.objects.create(bid_amount = 20000, fk_auction = a2, fk_user = u2)
Bid.objects.create(bid_amount = 25000, fk_auction = a2, fk_user = u3)
Bid.objects.create(bid_amount = 26000, fk_auction = a2, fk_user = u2)
Bid.objects.create(bid_amount = 31000, fk_auction = a2, fk_user = u3)


# Auction 3
Bid.objects.create(bid_amount = 20000, fk_auction = a3, fk_user = u4)
Bid.objects.create(bid_amount = 22000, fk_auction = a3, fk_user = u3)
Bid.objects.create(bid_amount = 25000, fk_auction = a3, fk_user = u1)
Bid.objects.create(bid_amount = 28000, fk_auction = a3, fk_user = u4)
Bid.objects.create(bid_amount = 30000, fk_auction = a3, fk_user = u1)
Bid.objects.create(bid_amount = 32000, fk_auction = a3, fk_user = u4)
Bid.objects.create(bid_amount = 38000, fk_auction = a3, fk_user = u3)
Bid.objects.create(bid_amount = 40000, fk_auction = a3, fk_user = u4)
Bid.objects.create(bid_amount = 45000, fk_auction = a3, fk_user = u1)
Bid.objects.create(bid_amount = 50000, fk_auction = a3, fk_user = u4)
Bid.objects.create(bid_amount = 53000, fk_auction = a3, fk_user = u1)


# Auction 4
Bid.objects.create(bid_amount = 3000, fk_auction = a4, fk_user = u1)
Bid.objects.create(bid_amount = 3100, fk_auction = a4, fk_user = u3)
Bid.objects.create(bid_amount = 3200, fk_auction = a4, fk_user = u1)
Bid.objects.create(bid_amount = 3500, fk_auction = a4, fk_user = u4)
Bid.objects.create(bid_amount = 4000, fk_auction = a4, fk_user = u3)
Bid.objects.create(bid_amount = 4200, fk_auction = a4, fk_user = u4)
Bid.objects.create(bid_amount = 4500, fk_auction = a4, fk_user = u1)
Bid.objects.create(bid_amount = 4800, fk_auction = a4, fk_user = u3)
Bid.objects.create(bid_amount = 5000, fk_auction = a4, fk_user = u1)
Bid.objects.create(bid_amount = 5500, fk_auction = a4, fk_user = u3)
Bid.objects.create(bid_amount = 6000, fk_auction = a4, fk_user = u1)
Bid.objects.create(bid_amount = 6400, fk_auction = a4, fk_user = u4)
