from django.db import models
import re
CURRENCY_REGEX = re.compile(r'^\d+(?:\.\d+)?')
YEAR_REGEX = re.compile(r'^(19|20)\d{2}$')

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

class Auction (models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100, default='other')
    duration_seconds = models.IntegerField()
    starting_bid = models.IntegerField()
    current_bid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuctionManager()
    # created_by = models.ForeignKey(User, related_name="created_auctions")
    def __repr__(self):
        return "<Auction object: title: {}, category: {}, description: {}, duratmediaion_seconds: {}, starting_bid: {}, current_bid: {}>".format(self.title, self.category, self.description, self.duration_seconds, self.starting_bid, self.current_bid)

class Media (models.Model):
    media_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    media_type = models.CharField(max_length=100)
    in_auction = models.ForeignKey(Auction, related_name="in_media")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MediaManager()
    def __repr__(self):
        return "<Media object: title: {}, genre: {}, release_year: {}, type: {}, in_auction: {}>".format(self.media_title, self.genre, self.release_year, self.type, self.in_auction)
