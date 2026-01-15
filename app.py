import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Health Chain",
    page_icon="🏥",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/Rd8GyFU.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **Health Chain** is a revolutionary health management platform that combines blockchain technology, advanced artificial intelligence, and accessibility to deliver secure, transparent, and patient-centric healthcare solutions with 45+ AI modes across 16 health modules.

    > The original version can be accessed here https://healtchain.elpeef.com/
    
    ---
    #### 🔮 Vision Statement
    
    To become Indonesia's leading AI-powered digital healthcare platform that empowers people with full control over their health data through blockchain technology and artificial intelligence.
    
    ---
    ### 🧩 Apps Showcase
    Our apps and tools can be seen here:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
    #### 🙌 Support & Contribute
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/healthchain)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

def embed_iframe(src, height=900):
    components.html(f"""
    <div style="width:100%; height:{height}px;">
        <iframe src="{src}"
                style="width:100%; height:100%; border:none; border-radius:12px;">
        </iframe>
    </div>
    """, height=height)

iframe_url = "https://healthchain.elpeef.com/"

embed_iframe(iframe_url, height=900)
