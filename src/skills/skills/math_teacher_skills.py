# 数智教师 Agent —— 36个核心技能（全部在一个文件）
class MathTeacherSkills:
    def __init__(self):
        pass

    # ==============================================
    # 1. 启发式提问引导（6个）
    # ==============================================
    def skill_ask_intro(self, question):
        return "【引导提问】我会一步步引导你思考，不直接给答案。"
    def skill_ask_step(self, question):
        return "【递进提问】请告诉我你做到哪一步，我继续引导你。"
    def skill_ask_hint(self, question):
        return "【卡壳提示】我给你一个小提示，你再试试看。"
    def skill_ask_no_answer(self, question):
        return "【拒绝直答】学习需要自己思考，我不能直接给答案哦。"
    def skill_ask_break(self, question):
        return "【拆解提问】我们把题目拆成小问题，一个一个解决。"
    def skill_ask_analogy(self, question):
        return "【类比提问】用生活例子帮你理解这个知识点。"
class MathTeacherSkills:
    def __init__(self):
        pass
   
    # ==========================
    # 2数学专业技能（10个）
    # ==========================
    def 高等数学演算与解题(self, user_input):
        return f"【技能启用】高等数学演算与解题：{user_input}"

    def 线性代数运算与分析(self, user_input):
        return f"【技能启用】线性代数运算与分析：{user_input}"

    def 概率统计计算与推断(self, user_input):
        return f"【技能启用】概率统计计算与推断：{user_input}"

    def 数学定理推导与严谨证明(self, user_input):
        return f"【技能启用】数学定理推导与严谨证明：{user_input}"

    def 数学概念通俗化讲解(self, user_input):
        return f"【技能启用】数学概念通俗化讲解：{user_input}"

    def 重难点梳理与考点归纳(self, user_input):
        return f"【技能启用】重难点梳理与考点归纳：{user_input}"

    def 错题归因与问题诊断(self, user_input):
        return f"【技能启用】错题归因与问题诊断：{user_input}"

    def 分层学情适配教学(self, user_input):
        return f"【技能启用】分层学情适配教学：{user_input}"

    def 大学期末习题精讲(self, user_input):
        return f"【技能启用】大学期末习题精讲：{user_input}"

    def 考研数学应试辅导(self, user_input):
        return f"【技能启用】考研数学应试辅导：{user_input}"
    
    # ==============================================
    # 3. MCP 调度会话管理（6个）
    # ==============================================
    def skill_mcp_intent(self, question):
        return "【调度】已识别你的学习意图。"
    def skill_mcp_context(self, question):
        return "【调度】多轮对话上下文已保存。"
    def skill_mcp_progress(self, question):
        return "【调度】学习进度已记录。"
    def skill_mcp_switch(self, question):
        return "【调度】已为你切换知识点讲解。"
    def skill_mcp_refuse(self, question):
        return "【调度】该问题无法直接回答，我引导你思考。"
    def skill_mcp_review(self, question):
        return "【调度】本次学习内容已复盘总结。"

    # ==============================================
    # 4. 长短期记忆认知（2个）
    # ==============================================
    def skill_memory_long(self, question):
        return "【记忆】你的学习薄弱点已长期保存。"
    def skill_memory_short(self, question):
        return "【记忆】当前对话上下文已记录。"

    # ==============================================
    # 5. 新对话生命周期（2个）
    # ==============================================
    def skill_session_new(self, question):
        return "【会话】全新对话已初始化。"
    def skill_session_recognize(self, question):
        return "【会话】已识别为继续历史对话。"

    # ==============================================
    # 6. 智能联网检索能力（2个）
    # ==============================================
    def skill_search_knowledge(self, question):
        return "【检索】正在联网查询权威知识点。"
    def skill_search_check(self, question):
        return "【检索】定理公式已完成权威校验。"
    
    # ==========================
    # 7.工具调用技能（6个）
    # ==========================
    def 本地知识库RAG检索(self, user_input):
        return f"【技能启用】本地知识库 RAG 检索：{user_input}"

    def 联网在线信息搜索(self, user_input):
        return f"【技能启用】联网在线信息搜索：{user_input}"

    def 智能工具调用路由(self, user_input):
        return f"【技能启用】智能工具调用路由：{user_input}"

    def 教材讲义资料调取(self, user_input):
        return f"【技能启用】教材讲义资料调取：{user_input}"

    def 真题题库查询匹配(self, user_input):
        return f"【技能启用】真题题库查询匹配：{user_input}"

    def 数学公式规范排版(self, user_input):
        return f"【技能启用】数学公式规范排版：{user_input}"