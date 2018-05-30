from django.db import models
import datetime
import re
CURRENCY_REGEX = re.compile(r'^\d+(?:\.\d+)?')
YEAR_REGEX = re.compile(r'^(19|20)\d{2}$')

# TODO: (Ver 2) Add level to Users and Auction, so only users that have same or higher level can participate the auction.


class AuctionManager(models.Manager):
    def auction_validator (self, requestPOST):
        errors = {}
        if len(requestPOST['title']) < 5:
            errors['title'] = "Title of auction must be at least 5 characters long."
        if len(requestPOST['description']) < 10:
            errors['description'] = "Description of auction should be at least 10 characters long."
        if len(requestPOST['duration']) < 1:
            errors['duration'] = "Duration cannot be left blank. Specify how many seconds long the promo is."
        if len(requestPOST['starting_bid']) < 1:
            errors['starting_bid'] = "Starting bid cannot be blank. Specify the dollar amount that the auction will start at."
        if not CURRENCY_REGEX.match(requestPOST['starting_bid']):
            errors['currency'] = "Starting bid must be in dollar format ($X.XX)."
        return errors


class MediaManager(models.Manager):
    def media_validator (self, requestPOST):
        errors = {}
        if len(requestPOST['media_title']) < 5:
            errors['media_title'] = "Title of media must be at least 5 characters long."
        if len(requestPOST['genre']) < 5:
            errors['genre'] = "Genre of media should be at least 5 characters long."
        if not YEAR_REGEX.match(requestPOST['release_year']):
            errors['release_year'] = "Year must be valid."
        return errors


class Genre (models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Genre object: genre_id {}, genre_name: {}>".format(self.genre_id, self.genre_name)


class Media (models.Model):
    media_id = models.AutoField(primary_key=True)
    media_title = models.CharField(max_length=255)
    fk_genre = models.ForeignKey(Genre, related_name="fk_media")
    release_year = models.IntegerField()
    media_type = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MediaManager()

    def __repr__(self):
        return "<Media object: media_id {}, media_title: {}, fk_genre: {}, release_year: {}, media_type: {}>".format(self.media_id, self.media_title, self.fk_genre, self.release_year, self.media_type)


class Category (models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Category object: category_id {}, category_name: {}>".format(self.category_id, self.category_name)


class Auction (models.Model):
    auction_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    duration_seconds = models.IntegerField()
    starting_bid = models.FloatField()
    current_bid = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(auto_now=True)
    fk_category = models.ForeignKey(Category, related_name="fk_auction", null=True)
    fk_media = models.ForeignKey(Media, related_name="fk_auction", null=True)
    # fk_user = models.ForeignKey(User, related_name="fk_auction")

    objects = AuctionManager()
    
    def __repr__(self):
        return "<Auction object: auction_id {}, title: {}, desciption: {}, duration: {}, starting_bid: {}, deadline: {}, fk_category: {}, fk_media: {}>".format(self.auction_id, self.title, self.description, self.duration_seconds, self.starting_bid, self.deadline, self.fk_category, self.fk_media)


class Bid (models.Model):
    bid_id = models.AutoField(primary_key=True)
    fk_auction = models.ForeignKey(Auction, related_name="fk_bid")
    # fk_user = models.ForeignKey(User, related_name="fk_auction")
    bid_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "<Bid object: bid_id {}>".format(self.bid_id, self.fk_auction)