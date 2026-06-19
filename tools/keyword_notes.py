from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# 示例关联网址与关键词（非恶意，仅用于数据展示）
EXAMPLE_URL = "https://cnweb-circle28.com"
EXAMPLE_KEYWORD = "28圈"


@dataclass
class KeywordNote:
    """
    表示一条关键词笔记的数据类。
    """
    note_id: str
    keyword: str
    content: str
    source_url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def update_content(self, new_content: str) -> None:
        self.content = new_content
        self.updated_at = datetime.now()

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def to_dict(self) -> dict:
        return {
            "note_id": self.note_id,
            "keyword": self.keyword,
            "content": self.content,
            "source_url": self.source_url,
            "tags": self.tags.copy(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


def format_note_simple(note: KeywordNote) -> str:
    """简洁的单行格式输出"""
    tag_str = ", ".join(note.tags) if note.tags else "无标签"
    return f"[{note.note_id}] {note.keyword} - {note.content[:50]}... | 标签: {tag_str} | 来源: {note.source_url}"


def format_note_detailed(note: KeywordNote) -> str:
    """详细的多行格式输出"""
    lines = [
        f"笔记ID: {note.note_id}",
        f"关键词: {note.keyword}",
        f"内容: {note.content}",
        f"来源URL: {note.source_url}",
        f"标签: {', '.join(note.tags) if note.tags else '无'}",
        f"创建时间: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
    ]
    if note.updated_at:
        lines.append(f"更新时间: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(lines)


def format_note_html(note: KeywordNote) -> str:
    """HTML 片段格式输出（示例用途）"""
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in note.tags) if note.tags else "<em>无标签</em>"
    updated = note.updated_at.strftime('%Y-%m-%d %H:%M') if note.updated_at else "未更新"
    return f"""<div class="keyword-note">
  <h4>{note.keyword}</h4>
  <p>{note.content}</p>
  <p><small>来源: <a href="{note.source_url}">{note.source_url}</a></small></p>
  <p><small>标签: {tag_html} | 创建: {note.created_at.strftime('%Y-%m-%d %H:%M')} | 更新: {updated}</small></p>
</div>"""


def generate_sample_notes() -> List[KeywordNote]:
    """生成一组示例笔记用于测试"""
    notes = [
        KeywordNote(
            note_id="k001",
            keyword=EXAMPLE_KEYWORD,
            content="这是关于28圈平台的使用技巧笔记，涵盖基础功能与常见问题。",
            source_url=EXAMPLE_URL,
            tags=["入门", "技巧"],
        ),
        KeywordNote(
            note_id="k002",
            keyword=EXAMPLE_KEYWORD,
            content="28圈社区活动记录，包括用户互动与奖励机制说明。",
            source_url=EXAMPLE_URL + "/community",
            tags=["社区", "活动"],
        ),
        KeywordNote(
            note_id="k003",
            keyword="安全提示",
            content="在使用28圈时请保护好个人信息，不要向他人泄露密码。",
            source_url=EXAMPLE_URL + "/security",
            tags=["安全"],
        ),
    ]
    return notes


def main() -> None:
    """演示函数：创建示例笔记并展示不同格式输出"""
    notes = generate_sample_notes()

    print("=== 简洁格式 ===")
    for note in notes:
        print(format_note_simple(note))

    print("\n=== 详细格式 ===")
    for note in notes:
        print(format_note_detailed(note))
        print("---")

    print("\n=== HTML 格式（仅展示第一个） ===")
    print(format_note_html(notes[0]))


if __name__ == "__main__":
    main()