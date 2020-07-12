from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app) # wrapping our app in an api

video_put_args = reqparse.RequestParser() # make new RequestParser object

# RequestParser
video_put_args.add_argument("name", type=str, help="Name of video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of video are required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of video are required", required=True)

videos = {}

class Video(Resource): # HelloWorld is a Resource class, we are inheriting
	def get(self, video_id): # overriding the get method
		return videos[video_id] # need key/value pair (HAS TO BE SERIALIZABLE!)

	def put(self, video_id):
		args = video_put_args.parse_args()
		videos[video_id] = args
		return videos[video_id], 201 # STATUS CODE 201='created'

api.add_resource(Video, "/video/<int:video_id>") # adding HelloWorld resource to the api. "/" is default, but if wanted reponse when user typed "HelloWorld" we would make it "/HelloWorld"

if __name__ == "__main__":
	app.run(debug=True) # this will start server and flask application in debug mode. will see all logging information. only for testing environment

