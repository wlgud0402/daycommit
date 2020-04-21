#페이지네이션

@app.route("/board", methods=['GET'])
def board():
    page = request.args.get("page") board에서 가져오는 page쿼리값
    if page == None:                page가 없다면 = 기본페이지라면>> 자연적으로 첫번째 1페이지를 보여줌
        page = 1  
    else:
        page = int(page)

    connection=getConnection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    #sql = "SELECT * FROM boards limit %s, 10"
    #                                                                                                    boards의 멤버id  = members의 id
    sql = "SELECT boards.id, boards.title, boards.content, members.user_name from boards join members on boards.member_id = members.id limit %s,10"
    cursor.execute(sql,((page-1)*10))
    rows = cursor.fetchall()
    
    sql = "SELECT COUNT(*) AS count FROM boards"
    cursor.execute(sql)
    result = cursor.fetchone()

    boardCount = result['count']
    pageCount = math.ceil(boardCount / 10)

    pages=[]
    for i in range(1, pageCount +1):
        pages.append(i)
    return render_template("board.html", boards=rows, pages=pages)