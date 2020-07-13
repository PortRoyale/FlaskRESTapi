from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) # wrapping our app in an api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # will make and save a db file in current directory
db = SQLAlchemy(app)

class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False) # 100 max characters and no empty names
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name={name}, views={views}, likes={likes})" # f strings print/insert what is in brackets


######
db.create_all() # DELETE THIS OR COMMENT IT OUT AFTER INITITIAL DB CREATION!!!! ONLY ONE TIME SHOULD IT BE RUN OR WILL OVERWRITE DATABASE



# RequestParser
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

# for Video.patch(video_id) to update only 'views' for example
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")


resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class Video(Resource): # Resource class, we are inheriting
	@marshal_with(resource_fields) # DECORATOR: this serializes every instance into a json format
	def get(self, video_id): # overriding the get method
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find video with that ID.")
		return result # need key/value pair (HAS TO BE SERIALIZABLE!)

	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message=f"Video ID {video_id} already in database.")

		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(video)
		db.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video doesn't exist, cannot update.")

		if args['name']: # if NOT none
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.add(result)
		db.session.commit()

		return result

	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204 # "Hey, it worked. Youw ere able to delete it."

	# def get_all(self):
	# 	for video_id in videos:
	# 		print(video_id)


api.add_resource(Video, "/video/<int:video_id>") # adding HelloWorld resource to the api. "/" is default, but if wanted reponse when user typed "HelloWorld" we would make it "/HelloWorld"

if __name__ == "__main__":
	app.run(debug=True) # this will start server and flask application in debug mode. will see all logging information. only for testing environment

