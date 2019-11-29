import hashlib

def bar():
    return 'hey everyone!'
    
def md5(password):
    if password:
        result = hashlib.md5(password.encode()).hexdigest()
        return result
        
def get_sports_name(sports_id):
    if sports_id:
        result = sports.find_one({"id":sports_id})
        return result
    else:
        return ""
        
def get_tournaments_name(tournament_id):
    if tournament_id:
        result = tournaments.find_one({"id":tournament_id})
        return result
    else:
        return ""
        
def get_players_name(player_id):
    if player_id:
        result = players.find_one({"id":player_id})
        return result
    else:
        return ""
        
def admin_data_upload():
    # check if the post request has the file part - Soccer Tournament
    if 'soccer_tournament' not in request.files:
        soccer_tournament = ""
    else:
        file = request.files['soccer_tournament']
        
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
        
            
            ###### Creating the first Dataframe using dictionary - EXCEL Upload
            data = pd.read_excel(file) 
            df = pd.DataFrame(data, columns= ['Product','Price'])
            print (df)
            
            #Process 1 -
            records = df.to_dict(orient = 'records')
            result = db.soccer_tournament.insert_many(records)
            
            #Process 2 -
            data_json = json.loads(df.to_json(orient='records'))
            db.soccer_tournament.insert(data_json)
            #################################################### - EXCEL Upload
            
            
            """
            ###### Creating the first Dataframe using dictionary - CSV Upload
            df1 = pd.read_csv(file)
            df1.dropna(how="all", inplace=True)
            print(df1)
            
            #Process 1 -
            records = df1.to_dict(orient = 'records')
            result = db.soccer_tournament.insert_many(records)
            
            #Process 2 -
            data_json = json.loads(df1.to_json(orient='records'))
            db.soccer_tournament.insert(data_json)
            #################################################### - CSV Upload
            """
            
        
            soccer_tournament = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], soccer_tournament))
            
    return soccer_tournament
    
def slugify(s, max_length=None):
    """ Transform a string to a slug that can be used in a url path.

    This method will first try to do the job with python-slugify if present.
    Otherwise it will process string by stripping leading and ending spaces,
    converting unicode chars to ascii, lowering all chars and replacing spaces
    and underscore with hyphen "-".

    :param s: str
    :param max_length: int
    :rtype: str
    """
    s = ustr(s)
    if slugify_lib:
        # There are 2 different libraries only python-slugify is supported
        try:
            return slugify_lib.slugify(s, max_length=max_length)
        except TypeError:
            pass
    uni = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    slug = re.sub('[\W_]', ' ', uni).strip().lower()
    slug = re.sub('[-\s]+', '-', slug)

    return slug[:max_length] 