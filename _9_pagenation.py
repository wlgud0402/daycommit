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
    cursor.execute(sql,((page-1)*10))   INNER JOIN 하고서의 테이블에 LIMIT 로 보여줄 갯수 제한하고서 가져옴
    rows = cursor.fetchall()
    
    sql = "SELECT COUNT(*) AS count FROM boards"    글의 갯수를 세줌
    cursor.execute(sql)
    result = cursor.fetchone()                      AS로 글의 갯수가 저장된 테이블이므로 행은 단 한개만 존재한다.

    boardCount = result['count']        COUNT 기능으로 만든 테이블의 컬럼명은 count로 지정되어 있다.
    pageCount = math.ceil(boardCount / 10)  필요한 페이지수를 구한다.

    pages=[]
    for i in range(1, pageCount +1):만약 글이 100 개가 있어서 pagecount가 10 이라면 range(1, 10 +1)페이지 추가> 1 번부터 10 번까지
        pages.append(i)
    return render_template("board.html", boards=rows, pages=pages)