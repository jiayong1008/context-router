# The Context Router

**A file pattern that lets any AI agent navigate your notes vault — without reading all of it every session.**

Works with Claude Code, Codex, Cursor, or anything else that reads a root instruction file. Plain markdown. No plugin, no lock-in, nothing to install.

---

## The problem

You point an AI agent at your notes and one of two things happens. Either it reads everything — slow, expensive, and it still surfaces the wrong details — or it reads nothing useful and you spend the first five minutes of every session re-explaining who you are and what you're working on.

## The fix

Split context into two layers:

- **Always loaded** — a short index of who you are and what's active. Capped by rule at about one screen.
- **Loaded on demand** — one deep file per project, opened only when that project actually comes up.

A routing table connects them: trigger words → file path. The agent reads the index, matches what you typed, opens exactly one file.

Ten projects or forty, a conversation costs the same. The router just has more rows.

---

## Setup — about 15 minutes

**Step 1 is the same for everyone:** copy these files into the root of your notes vault — the folder that contains your project folders.

Then pick the path that matches how you use AI. Both end up in the same place.

### Path A — you use an AI agent that reads your files

*Claude Code, Codex, Cursor, or anything else that opens a folder on your computer.*

Open your agent **in your vault folder** and say:

> Read "01 START HERE" and set this up with me.

It interviews you and writes everything. That's the whole setup.

### Path B — you use AI in a browser or desktop app

*Claude, ChatGPT, Gemini — anything where you chat in a window and upload files.*

Your AI can't reach your folder, so you hand it the files instead:

1. Start a new chat — or better, a **Project** if your tool has them (Claude Projects, ChatGPT Projects). A Project keeps the context across every future chat instead of just one.
2. Upload `01 START HERE`, `CLAUDE.md`, `MEMORY.md`, and `_TEMPLATE_CONTEXT.md`.
3. Say: *"Read the START HERE file and set this up with me."*
4. It interviews you the same way, then gives you finished files to **save into your vault yourself** — copy each one into the folder it names.

From then on, upload or paste `MEMORY.md` plus the one relevant `_CONTEXT.md` at the start of a conversation. More manual than Path A, same benefit: the AI gets exactly the context it needs and nothing else.

> **Worth knowing:** Path B is where most people start, and it's completely fine.
> If you later move to a file-reading agent, everything you built still works —
> that's the point of keeping it in plain markdown.

### Then, either way

**Test it cold.** New session, ask *"what's the status on [project]?"* using only a trigger word — no file path. If it pulls the right context and answers from it, you're done.

No configuration file, no API key, no plugin, nothing to install.

---

## What's in here

| File | What it does |
| :--- | :--- |
| `01 START HERE` | The interview script your agent runs to set everything up. Delete when done, or keep for adding projects later. |
| `CLAUDE.md` | Rules + the routing table. The file agents read first. |
| `AGENTS.md` | A pointer to `CLAUDE.md`, for tools that look for this filename instead. |
| `MEMORY.md` | Your always-loaded index. Keep it to one screen. |
| `_TEMPLATE_CONTEXT.md` | The shape every project's context file takes. |
| `Projects/_EXAMPLE Nova/` | A filled-in example so you can see what a real one looks like. Delete it. |

---

## Keeping it alive

The pattern is easy. The upkeep is the actual work, and it's small:

- Say **"remember this"** mid-conversation — the agent knows which file it belongs in.
- Let the agent **update the project file** when something changes, deleting what stopped being true in the same pass.
- **New project → three things**: its context file, a routing row, a memory line. The rules tell the agent to do all three unprompted.
- **Once a month, skim the routing table.** Remove dead projects, index anything that got created live. Five minutes.

That last one matters. Things created mid-session sometimes never get indexed — this drift is normal, and the monthly skim is the fix, not a sign the system failed.

---

## Honest limits

- **This is keyword matching, not search.** No embeddings, no ranking. That's fine at personal-vault scale and a real ceiling past a few dozen projects.
- **It's maintained by hand.** Nothing enforces the routing table. It stays accurate because you and the agent keep updating it.
- **Your tool has to read a root instruction file.** Most agent CLIs do. If yours doesn't, paste `CLAUDE.md` in at session start — still useful, just less automatic.
- **It's discipline encoded as file structure.** If you wouldn't keep a project README current, this will rot for the same reason. The pattern doesn't create the habit; it makes the habit pay off.

---

*Built by Lim Jia Yong — software engineering lead, Malaysia. I build practical AI and automation systems, and this is the setup I actually run.*

*[@JiaYongLim1008 on X](https://x.com/JiaYongLim1008) · [GitHub](https://github.com/jiayong1008) · [LinkedIn](https://www.linkedin.com/in/lim-jia-yong/)*

*Copy it, fork it, change it. No permission needed.*
