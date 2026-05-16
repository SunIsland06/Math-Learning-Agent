# MCP 调度中心 —— 自动调用你所有 36 个技能
from skills import MathTeacherSkills

class MCP:
    def __init__(self):
        # 加载你所有的技能
        self.skills = MathTeacherSkills()

    # 技能调度入口
    def dispatch(self, user_input):
        # 统一处理用户输入
        text = user_input

        # ======================
        # 1. 启发式提问引导（6个）
        # ======================
        if "引导" in text or "不直接给答案" in text:
            return self.skills.skill_ask_intro(text)
        elif "递进" in text or "做到哪一步" in text:
            return self.skills.skill_ask_step(text)
        elif "提示" in text or "卡壳" in text:
            return self.skills.skill_ask_hint(text)
        elif "不直接给答案" in text or "拒绝" in text:
            return self.skills.skill_ask_no_answer(text)
        elif "拆解" in text or "拆成小问题" in text:
            return self.skills.skill_ask_break(text)
        elif "类比" in text or "例子" in text:
            return self.skills.skill_ask_analogy(text)

        # ======================
        # 2. 数学专业技能（10个）
        # ======================
        elif "高等数学" in text or "高数" in text or "演算" in text:
            return self.skills.高等数学演算与解题(text)
        elif "线性代数" in text or "线代" in text:
            return self.skills.线性代数运算与分析(text)
        elif "概率" in text or "统计" in text:
            return self.skills.概率统计计算与推断(text)
        elif "定理" in text or "证明" in text:
            return self.skills.数学定理推导与严谨证明(text)
        elif "概念" in text or "讲解" in text:
            return self.skills.数学概念通俗化讲解(text)
        elif "重点" in text or "考点" in text or "重难点" in text:
            return self.skills.重难点梳理与考点归纳(text)
        elif "错题" in text or "诊断" in text:
            return self.skills.错题归因与问题诊断(text)
        elif "分层" in text or "学情" in text or "适配" in text:
            return self.skills.分层学情适配教学(text)
        elif "期末" in text or "习题精讲" in text:
            return self.skills.大学期末习题精讲(text)
        elif "考研" in text or "应试" in text:
            return self.skills.考研数学应试辅导(text)

        # ======================
        # 3. MCP 调度会话管理（6个）
        # ======================
        elif "意图" in text or "识别" in text:
            return self.skills.skill_mcp_intent(text)
        elif "上下文" in text:
            return self.skills.skill_mcp_context(text)
        elif "进度" in text:
            return self.skills.skill_mcp_progress(text)
        elif "切换" in text or "知识点" in text:
            return self.skills.skill_mcp_switch(text)
        elif "无法回答" in text or "拒答" in text:
            return self.skills.skill_mcp_refuse(text)
        elif "复盘" in text or "总结" in text:
            return self.skills.skill_mcp_review(text)

        # ======================
        # 4. 长短期记忆（2个）
        # ======================
        elif "长期记忆" in text or "薄弱点" in text:
            return self.skills.skill_memory_long(text)
        elif "短期记忆" in text or "当前对话" in text:
            return self.skills.skill_memory_short(text)

        # ======================
        # 5. 新对话生命周期（2个）
        # ======================
        elif "新对话" in text or "初始化" in text:
            return self.skills.skill_session_new(text)
        elif "历史对话" in text or "继续" in text:
            return self.skills.skill_session_recognize(text)

        # ======================
        # 6. 智能联网检索（2个）
        # ======================
        elif "联网" in text or "搜索知识" in text:
            return self.skills.skill_search_knowledge(text)
        elif "校验" in text or "公式" in text or "定理" in text:
            return self.skills.skill_search_check(text)

        # ======================
        # 7. 工具调用技能（6个）
        # ======================
        elif "RAG" in text or "本地知识库" in text:
            return self.skills.本地知识库RAG检索(text)
        elif "在线搜索" in text or "联网搜索" in text:
            return self.skills.联网在线信息搜索(text)
        elif "工具" in text or "路由" in text:
            return self.skills.智能工具调用路由(text)
        elif "教材" in text or "讲义" in text:
            return self.skills.教材讲义资料调取(text)
        elif "真题" in text or "题库" in text:
            return self.skills.真题题库查询匹配(text)
        elif "公式" in text or "排版" in text:
            return self.skills.数学公式规范排版(text)

        # 默认回复
        else:
            return "【数智教师】我已准备就绪，请告诉我你的学习需求~"